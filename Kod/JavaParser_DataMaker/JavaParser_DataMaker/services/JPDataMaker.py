from Core.services.DataMaker import DataMaker
from Core.base.Graph import Graph

import JavaParser_DataMaker.plyj.parser as plyj
import JavaParser_DataMaker.plyj.model as m

from JavaParser_DataMaker.extended.ClassNode import ClassNode
from JavaParser_DataMaker.extended.InterfaceNode import InterfaceNode
from JavaParser_DataMaker.extended.ExtendsEdge import ExtendsEdge
from JavaParser_DataMaker.extended.AttributeEdge import AttributeEdge
from JavaParser_DataMaker.extended.ImplementsEdge import ImplementsEdge

from django.apps.registry import apps


class JPDataMaker(DataMaker):

    def __init__(self):
        super(JPDataMaker, self).__init__('JavaParser Data maker', 'java_parser')
        self.files = []

    def create_data(self):
        g = Graph()
        parser = plyj.Parser()

        # 1. pass - creating nodes
        for file in self.files:
            tree = parser.parse_string(file)

            for type_decl in tree.type_declarations:
                node = self.__create_node(type_decl)
                if node is not None:
                    g.add_node(node)

        # 2. pass - creating edges
        for file in self.files:
            tree = parser.parse_string(file)

            for type_decl in tree.type_declarations:
                if type(type_decl) is m.ClassDeclaration:
                    node = self._get_ClassNode(g, type_decl.name)

                    # Extends edge
                    if type_decl.extends is not None:
                        parent_node = self._get_ClassNode(g, type_decl.extends.name.value)
                        edge = ExtendsEdge(node1=node, node2=parent_node)
                        g.add_edge(edge)

                    # Implements edge
                    if len(type_decl.implements) is not 0:
                        for interface in type_decl.implements:
                            interface_node = self._get_InterfaceNode(g, interface.name.value)
                            if interface_node is not None:
                                edge = ImplementsEdge(node1=node, node2=interface_node)
                                g.add_edge(edge)


                    for declaration in type_decl.body:
                        # Contains edge - attributes
                        if type(declaration) is m.FieldDeclaration:
                            for var_decl in declaration.variable_declarators:
                                if type(declaration.type) is str:
                                    type_name = declaration.type
                                else:
                                    type_name = declaration.type.name.value

                                attribute_node = self._get_AttirubteNode(g, type_name)
                                if attribute_node is not None:
                                    edge = AttributeEdge(node1=node, node2=attribute_node)
                                    g.add_edge(edge)

        apps.get_app_config('Core').graph = g

    def save_data(self):
        pass

    def load_data(self):
        pass

    def send_data(self, files):
        self.files = files

    def __create_node(self, type_decl):
        if type(type_decl) is m.ClassDeclaration:
            node = ClassNode(nodeName=type_decl.name)

            for declaration in type_decl.body:
                # extracting attributes
                if type(declaration) is m.FieldDeclaration:
                    attribute = self.__extract_attribute(declaration)
                    node.add_attribute(attribute)
                # extracting methods
                elif type(declaration) is m.MethodDeclaration:
                    method = self.__extract_method(declaration)
                    node.add_method(method)
            return node

        elif type(type_decl) is m.InterfaceDeclaration:
            node = InterfaceNode(nodeName=type_decl.name)

            for declaration in type_decl.body:
                # extracting methods
                if type(declaration) is m.MethodDeclaration:
                    method = self.__extract_method(declaration)
                    node.add_method(method)
            return node

    def __extract_attribute(self, decl):
        for var_decl in decl.variable_declarators:
            if type(decl.type) is str:
                type_name = decl.type
            else:
                type_name = decl.type.name.value
        return type_name + ' ' + var_decl.variable.name

    def __extract_method(self, decl):
        params = []
        for param in decl.parameters:
            if type(param.type) is str:
                params.append(param.type + ' ' + param.variable.name)
            else:
                params.append(param.type.name.value + ' ' + param.variable.name)

        if type(decl.return_type) is str:
            return_type = decl.return_type
        else:
            return_type = decl.return_type.name.value

        if return_type is None:
            return decl.name + '(' + ','.join(params) + ')'
        else:
            return return_type + ' ' + decl.name + '(' + ','.join(params) + ')'

    def _get_ClassNode(self, g, node_name):
        for nodeType in g.nodes:
            for node in g.nodes[nodeType]:
                if node.name == node_name:
                    return node

        # node that is not yet defined - if class is extending class that was not defined by the user
        new_node = ClassNode(nodeName=node_name)
        g.add_node(new_node)
        return new_node

    def _get_InterfaceNode(self, g, node_name):
        for nodeType in g.nodes:
            for node in g.nodes[nodeType]:
                if node.name == node_name:
                    return node

        # node that is not yet defined - if class is implementing interface that was not defined by the user
        new_node = InterfaceNode(nodeName=node_name)
        g.add_node(new_node)
        return new_node

    def _get_AttirubteNode(self, g, node_name):
        for nodeType in g.nodes:
            for node in g.nodes[nodeType]:
                if node.name == node_name:
                    return node

from Core.base.abstract.Models import Node, Edge
import jsonpickle


class Graph:

    def __init__(self):
        """Graph initialization method."""
        super(Graph, self).__init__()
        self._nodes = {}
        self._edges = {}

    @property
    def nodes(self):
        """ Returns graph nodes
        :returns: Dictionary of all nodes in graph
        :rtype: dict{NodeType: list[Node]}"""
        return self._nodes

    @nodes.setter
    def nodes(self, value: dict):
        """Sets graph nodes
        :param value: New nodes
        :type value: dict{NodeType: list[Node]}"""
        self._nodes = value

    @property
    def edges(self):
        """ Returns graph edges
        :returns: Dictionary of all edges in graph
        :rtype: dict{EdgeType: list[Edge]}"""
        return self._edges

    @edges.setter
    def edges(self, value: dict):
        """Sets graph edges
        :param value: New edges
        :type value: dict{EdgeType: list[Edge]}"""
        self._edges = value

    def add_nodes(self, value: list):
        """Adds nodes from list to graph
        :param value: List of nodes
        :type value: list"""
        for node in value:
            self.add_node(node)

    def add_node(self, value: Node):
        """Adds node to graph
        :param value: Node added to graph
        :type value: Node"""
        node_type = value.__class__.__name__
        if node_type in self._nodes.keys():
            self._nodes.get(node_type).append(value)
        else:
            self._nodes[node_type] = []
            self._nodes.get(node_type).append(value)

    def add_edges(self, value: list):
        """Adds edges from list to graph
        :param value: List of edges
        :type value: list"""
        for edge in value:
            self.add_edge(edge)

    def add_edge(self, value: Edge):
        """Adds edge to graph
        :param value: Edge added to graph
        :type value: Edge"""
        edge_type = value.__class__.__name__
        if edge_type in self._edges.keys():
            self._edges.get(edge_type).append(value)
        else:
            self._edges[edge_type] = []
            self._edges.get(edge_type).append(value)

    def filter_nodes(self, *args):
        """Filters nodes based on given node types
        :param args: List of node types
        :type args: list
        :returns: Filtered list of nodes
        :rtype: list"""
        return [self._nodes.get(arg) for arg in args if arg in self._nodes]

    def filter_edges(self, *args):
        """Filters edges based on given edge types
        :param args: List of edge types
        :type args: list
        :returns: Filtered list of edges
        :rtype: list"""
        return [self._edges.get(arg) for arg in args if arg in self._edges]

    def to_json(self):
        node_dict = {}
        edge_dict = {}

        for key, value in self.nodes.items():
            new_list = []
            for item in value:
                new_list.append(item.to_json())
            node_dict[key] = new_list

        for key, value in self.edges.items():
            new_list = []
            for item in value:
                new_list.append(item.to_json())
            edge_dict[key] = new_list
        return {"nodes": node_dict, "edges": edge_dict}


def serialize(graph: Graph):
    """Serializes graph as JSON file
    :param graph: Graph written from
    :value graph: Graph
    """
    graph_json = jsonpickle.encode(graph)
    return graph_json


def deserialize(graph_json: str):
    """Deserializes JSON file as graph
    :param graph_json: Content of json file
    :value path: str"""
    graph = jsonpickle.decode(graph_json)
    return graph

from Core.base.abstract.Models import Node

class ClassNode(Node):

    def __init__(self, **kwargs):
        super(ClassNode, self).__init__(**kwargs)
        self._attributes = []
        self._methods = []
        self._implements = []

    def add_attribute(self, attr):
        self._attributes.append(attr)

    def add_method(self, method):
        self._methods.append(method)

    def add_implements(self, interface):
        self._implements.append(interface)

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value: set):
        self._attributes = value

    @property
    def methods(self):
        return self._methods

    @methods.setter
    def methods(self, value: set):
        self._methods = value

    @property
    def implements(self):
        return self._implements

    @implements.setter
    def implements(self, value: set):
        self._implements = value

    def get_data(self):
        return {
            "attributes": self._attributes,
            "methods": self._methods,
            "implements": self._implements
        }

from Core.base.abstract.Models import Node

class InterfaceNode(Node):

    def __init__(self, **kwargs):
        super(InterfaceNode, self).__init__(**kwargs)
        self._methods = []

    def add_method(self, method):
        self._methods.append(method)

    def get_data(self):
        return {
            "methods": self._methods
        }
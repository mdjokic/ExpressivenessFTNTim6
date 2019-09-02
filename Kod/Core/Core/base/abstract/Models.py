from abc import ABC, abstractmethod
from uuid import uuid4


class Node(ABC):

    @abstractmethod
    def __init__(self, **kwargs):
        """Node initialization method.
        :param nodeName: Sets node name
        :type nodeName: str
        :param isTerminal: Sets node terminal status
        :type isTerminal: bool
        :param nodeEdges: Sets adjacent node edges
        :type nodeEdges: set
        """
        super(Node, self).__init__()
        self._id = uuid4()
        self._name = kwargs.get("nodeName", None)
        self._terminal = kwargs.get("isTerminal", True)

    @property
    def id(self):
        """Returns unique node identifier.
        Unique id is implemented with 'A Universally Unique IDentifier' object.
        :returns: Node unique identifier
        :rtype: uuid.UUID"""
        return self._id

    @property
    def name(self):
        """Returns the node name.
        :returns: Node name
        :rtype: str"""
        return self._name

    @name.setter
    def name(self, value: str):
        """Sets the node name.
        :param value: Node name
        :type value: str"""
        self._name = value

    @property
    def terminal(self):
        """Returns node whether a node is terminal.
        Terminal nodes have no children associated with them in a tree view.
        :returns: Node terminal check
        :rtype: bool"""
        return self._terminal

    @terminal.setter
    def terminal(self, value: bool):
        """Sets the node terminal status.
        :param value: Node terminal status
        :type value: bool"""
        self._terminal = value

    def to_json(self): 
        return {
            "id": self.id,
            "name": self.name,
            "data": self.get_data()
        }

    @abstractmethod
    def get_data(self):
        """Returns all necessary node data."""
        pass

    def __str__(self):
        """Returns node string representation.
        :returns: Node name
        :rtype: str"""
        return self.name

    def __eq__(self, other):
        """Compares ids of two nodes.
        :returns: Equality check
        :rtype: bool"""
        if isinstance(other, Node):
            return self._id == other.id
        return False


class Edge(ABC):

    @abstractmethod
    def __init__(self, **kwargs):
        """Edge initialization method.
        :param weight: Sets edge weight
        :type weight: number
        :param node1: Sets first (from-) node
        :type node1: Node
        :param node2: Sets second (to-) node
        :type node2: Node
        """
        super(Edge, self).__init__()
        self._id = uuid4()
        self._weight = kwargs.get("weight", None)
        self._node1 = kwargs.get("node1", None)
        self._node2 = kwargs.get("node2", None)

    @property
    def id(self):
        """Returns unique edge identifier.
        Unique id is implemented with 'A Universally Unique IDentifier' object.
        :returns: Edge unique identifier
        :rtype: uuid.UUID"""
        return self._id

    @property
    def weight(self):
        """Returns edge weight.
        If the graph is weighted, edge weight is used to determine the importance of it.
        :returns: Edge weight
        :rtype: number"""
        return self._weight

    @weight.setter
    def weight(self, value: float):
        """Sets the edge weight.
        :param value: Edge weight
        :type value: number"""
        self._weight = value

    @property
    def node1(self):
        """Returns edge first node.
        If the graph is directional, first node will be the starting point.
        :returns: Edge first node
        :rtype: Node"""
        return self._node1

    @node1.setter
    def node1(self, value: Node):
        """Sets the edge first node.
        :param value: First (from-) node
        :type value: Node"""
        self._node1 = value

    @property
    def node2(self):
        """Returns edge second node.
        If the graph is directional, second node will be the starting point.
        :returns: Edge second node
        :rtype: Node"""
        return self._node2

    @node2.setter
    def node2(self, value: Node):
        """Sets the edge second node.
        :param value: Second (to-) node
        :type value: Node"""
        self._node2 = value

    def to_json(self):
        return{
            "id": self.id,
            "node1": self.node1.id,
            "node2": self.node2.id
        }

    def __str__(self):
        """Returns string representation of which nodes are connected.
        :returns: Edge with connected nodes
        :rtype: str"""
        return "EDGE: " + str(self.node1) + " - " + str(self.node2)

    def __hash__(self):
        """Needed so that edges can be added to sets.
        :returns: Hash value
        :rtype: number"""
        return hash(self._id)

    def __eq__(self, other):
        """Compares ids of two edges.
        :returns: Equality check
        :rtype: bool"""
        if isinstance(other, Edge):
            return self._id == other.id
        return False

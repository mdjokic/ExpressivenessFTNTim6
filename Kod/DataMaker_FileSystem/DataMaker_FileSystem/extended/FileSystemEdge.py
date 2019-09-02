from Core.base.abstract.Models import Edge


class FileSystemEdge(Edge):

    def __init__(self, **kwargs):
        super(FileSystemEdge, self).__init__(**kwargs)

    def __str__(self):
        return "Node1: " + str(self.node1) + " Node2: " + str(self.node2)
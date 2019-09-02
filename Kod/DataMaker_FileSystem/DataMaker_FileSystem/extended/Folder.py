from Core.base.abstract.Models import Node

class Folder(Node):


    def __init__(self, **kwargs):
        super(Folder, self).__init__(**kwargs)
        self.directory = ''
        self.ctime = kwargs.get('ctime')
        self.mtime = kwargs.get('mtime')

    def get_data(self):
        return {
            'Directory': self.directory,
            'Created': self.ctime,
            'Modified': self.mtime
        }

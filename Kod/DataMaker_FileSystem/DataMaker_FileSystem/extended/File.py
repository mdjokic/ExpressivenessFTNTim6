from Core.base.abstract.Models import Node
import time

class File(Node):

    def __init__(self, **kwargs):
        super(File, self).__init__(**kwargs)
        self.extension = kwargs.get('extension')
        self.directory = kwargs.get('directory')
        self.size = kwargs.get('size')
        self.ctime = kwargs.get('ctime')
        self.mtime = kwargs.get('mtime')

    def get_data(self):
        return {
            'Name': self.name,
            'Extension': self.extension,
            'Directory': self.directory,
            'Size': str(self.size) + "KB",
            'Created':self.ctime,
            'Modified':self.mtime
        }

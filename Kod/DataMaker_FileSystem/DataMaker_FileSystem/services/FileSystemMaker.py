from Core.services.DataMaker import DataMaker
from Core.base.Graph import Graph
from DataMaker_FileSystem.extended.File import File
from DataMaker_FileSystem.extended.Folder import Folder
from DataMaker_FileSystem.extended.FileSystemEdge import FileSystemEdge
from django.apps.registry import apps
from pathlib import Path
import os
import time

class FileSystemMaker(DataMaker):

    def __init__(self):
        super(FileSystemMaker, self).__init__('File system Data maker', 'filesystem')
        self.path = ""
        
    def create_data(self):
        KB = 1024
        nodeRestriction = 175
        count = 0
        graph = Graph()
        print(self.path)
        p = Path(self.path)
        nodes = dict()
        for item in os.walk(p):
            folder = Path(item[0])
            fullPath = folder.absolute()
            fullPathStr = fullPath.as_posix()
            if fullPathStr in nodes:
                node = nodes.get(fullPathStr)
            else:
                if(folder.name != ""):
                    if(folder.name[0] == "." or folder.name[0] == "$"):
                            continue
                node = Folder(nodeName = folder.name)
                node.directory = str(folder.parent.absolute())
                node.ctime = time.ctime(folder.stat().st_ctime)
                node.mtime = time.ctime(folder.stat().st_mtime)
                graph.add_node(node)
                count += 1
                if(folder.name == ""):
                    node.name = folder.absolute().as_posix()[0] + ":"
    
            for subFolderPath in item[1]:
                if(count > nodeRestriction):
                    break
                subFolder = folder.joinpath(subFolderPath)
                if(subFolder.name != ""):
                    if(subFolder.name[0] == "." or subFolder.name[0] == "$"):
                        continue
                folderNode = Folder(nodeName = subFolder.name)
                folderNode.directory = str(subFolder.parent.absolute())
                folderNode.ctime = time.ctime(subFolder.stat().st_ctime)
                folderNode.mtime = time.ctime(subFolder.stat().st_mtime)
                graph.add_node(folderNode)
                count += 1
                edge = FileSystemEdge(node1 = node, node2 = folderNode)
                graph.add_edge(edge)
                fullPath = subFolder.absolute()
                fullPathStr = fullPath.as_posix()
                nodes[fullPathStr] = folderNode

            for filePath in item[2]:
                if(count > nodeRestriction):
                    break
                file = folder.joinpath(filePath)
                if(file.name != ""):
                    if(file.name[0] == "." or file.name[0] == "$"):
                        continue
                fileNode = File(nodeName = file.stem)
                fileNode.extension = file.suffix
                fileNode.directory = str(file.parent.absolute())
                fileNode.size = round(file.stat().st_size/ KB,2)
                fileNode.ctime = time.ctime(file.stat().st_ctime)
                fileNode.mtime = time.ctime(file.stat().st_mtime)
                graph.add_node(fileNode)
                count += 1
                edge = FileSystemEdge(node1 = node, node2 = fileNode)
                graph.add_edge(edge)
            if(count > nodeRestriction):
                break
        apps.get_app_config('Core').graph = graph
        
    def save_data(self):
        pass

    def load_data(self):
        pass

    def send_data(self, path):
        self.path = path
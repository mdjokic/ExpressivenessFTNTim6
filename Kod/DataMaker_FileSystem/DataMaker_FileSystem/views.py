from django.apps.registry import apps
from django.shortcuts import render, redirect
from pathlib import Path
from DataMaker_FileSystem.services.FileSystemMaker import FileSystemMaker


def index(request):
    return render(request, 'DataMaker_FileSystem/index.html',{"greska":False})

def createGraph(request):
    path = request.POST["path"]
    if(Path(path).exists() == False or Path(path).is_dir() == False):
        return redirect("..")
        
    fileSystemMaker = FileSystemMaker()
    fileSystemMaker.send_data(path)
    fileSystemMaker.create_data()
    return redirect('../../core/visualization')

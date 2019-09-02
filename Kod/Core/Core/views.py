from django.apps.registry import apps
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.datastructures import MultiValueDictKeyError

from Core.base.Graph import deserialize, serialize, Graph

def index(request):
    data_plugins = apps.get_app_config('Core').data_plugins
    return render(request, 'core/index.html', {"data_plugins": data_plugins})

def visualization(request):
    visualization_plugins = apps.get_app_config('Core').visualization_plugins
    return render(request, 'core/visualization.html', {"visualization_plugins": visualization_plugins})

def getGraph(request):
    graph = apps.get_app_config('Core').graph
    if graph is None:
        graph = Graph()
    return JsonResponse({"graph": graph.to_json()})

def uploadData(request):
    try:
        if request.method == 'POST' and request.FILES['file']:
            dataFile = request.FILES['file']
            dataFile = dataFile.read().decode('ansi', 'strict')

            graph = deserialize(dataFile)
            apps.get_app_config('Core').graph = graph

            return redirect('/core/visualization')
    except MultiValueDictKeyError:
        graph = Graph()
        apps.get_app_config('Core').graph = graph
        return redirect('/core/visualization')

def saveData(request):
    graph = apps.get_app_config('Core').graph
    return JsonResponse({"graph": serialize(graph)})

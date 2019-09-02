from django.apps.registry import apps
from django.shortcuts import render

def index(request):
    visualization_plugins = apps.get_app_config('Core').visualization_plugins
    return render(request, 'DetailedVisualizator/detailed.html', {"visualization_plugins": visualization_plugins})

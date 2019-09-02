from django.apps.registry import apps
from django.shortcuts import render, redirect
from DataMaker_IMDB.services.IMDBMaker import IMDBMaker


def index(request):
    return render(request, 'DataMaker_IMDB/index.html')

def makeData(request):
    payload = dict()
    persons = set()
    maker = IMDBMaker()

    for key in request.POST.keys():
        if key.startswith('personField'):
            if request.POST[key] and (not request.POST[key].isspace()):
                persons.add(request.POST[key])
    
    payload['persons'] = persons
    payload['yearMin'] = request.POST["yearMin"]
    payload['yearMax'] = request.POST["yearMax"]
    maker.send_data(payload)
    maker.create_data()
    return redirect('../../core/visualization')

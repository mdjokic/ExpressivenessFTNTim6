from django.shortcuts import render, redirect
from JavaParser_DataMaker.services.JPDataMaker import JPDataMaker


def index(request):
    return render(request, 'JavaParser_DataMaker/index.html')


def project_upload(request):
    dm = JPDataMaker()
    java_files = []

    if request.method == 'POST':
        files = request.FILES.getlist('file')
        for f in files:
            if f.name.endswith('.java'):
                file = f.read().decode('ansi', 'strict') # decoding InMemoryUploadedFile
                java_files.append(file)

        dm.send_data(java_files)
        dm.create_data()

        return redirect('../../core/visualization')


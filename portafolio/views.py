from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def proyectos(request):
    #projects = [
    #    { "title": "Proyecto 1", "description": "Descripción del proyecto 1", "in_progress": True, "image1": "" },
    #    { "title": "Proyecto 2", "description": "Descripción del proyecto 2", "in_progress": False, "image2": "" },
    #    { "title": "Proyecto 3", "description": "Descripción del proyecto 3 ", "in_progress": True, "image3": "" },
    #]
    return render(request, 'proyectos.html')

def contacto(request):
    return render(request, 'contacto.html')
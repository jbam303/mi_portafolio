from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    hora = datetime.now().hour
    if hora < 12:
        saludo = "Buenos días!!"
    elif hora < 19:
        saludo = "Buenas tardes!!"
    else:
        saludo = "Buenas noches!!"
    return render(request, 'index.html', {'saludo': saludo})

def proyectos(request):
    projects = [
        { "title": "Proyecto 1", "description": "Descripción del proyecto 1", "in_progress": True, "image": "images/johan.jpg" },
        { "title": "Proyecto 2", "description": "Descripción del proyecto 2", "in_progress": False, "image": "images/johan.jpg" },
        { "title": "Proyecto 3", "description": "Descripción del proyecto 3 ", "in_progress": True, "image": "images/johan.jpg" }
    ]
    return render(request, 'proyectos.html', {'projects': projects})

def contacto(request):
    return render(request, 'contacto.html')
from django.shortcuts import render
from django.templatetags.static import static
from datetime import datetime

# Create your views here.
def index(request):
    hora = datetime.now().hour
    if hora < 12 and hora >= 6:
        fondo = static("images/fondo-amanecer.png")
        saludo = "Buenos días!!"
    elif hora > 12 and hora < 19:
        fondo = static("images/fondo-atardecer.png")
        saludo = "Buenas tardes!!"
    else:
        fondo = static("images/fondo-anochecer.png")
        saludo = "Buenas noches!!"
    return render(request, 'index.html', {'saludo': saludo, 'fondo': fondo})



def proyectos(request):
    projects = [
        { "title": "Proyecto 1", "description": "Descripción del proyecto 1", "in_progress": True, "image": "images/johan.jpg" },
        { "title": "Proyecto 2", "description": "Descripción del proyecto 2", "in_progress": False, "image": "images/johan.jpg" },
        { "title": "Proyecto 3", "description": "Descripción del proyecto 3 ", "in_progress": True, "image": "images/johan.jpg" }
    ]
    return render(request, 'proyectos.html', {'projects': projects})

def contacto(request):
    return render(request, 'contacto.html')
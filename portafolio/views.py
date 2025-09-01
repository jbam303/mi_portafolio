from django.shortcuts import render
from django.templatetags.static import static
from datetime import datetime

# Create your views here.
def index(request):
    hora = datetime.now().hour
    if hora >= 6 and hora <= 12:
        fondo = static("images/fondo-amanecer.png")
        saludo = "Buenos días!!"
    elif hora > 12 and hora <= 19:
        fondo = static("images/fondo-atardecer.png")
        saludo = "Buenas tardes!!"
    else:
        fondo = static("images/fondo-anochecer.png")
        saludo = "Buenas noches!!"
    return render(request, 'index.html', {'saludo': saludo, 'fondo': fondo})

projects = [
        { "title": "Ayuda Gestor Stock", "description": "Aplicacion para ayudar a gestionar el stock en Botilleria HangaRoa", "in_progress": True, "image": "images/gestor-stock.png" },
        { "title": "Calculadora", "description": "Pequeña calculadora con interfaz grafica con pyside", "in_progress": True, "image": "images/Calculadora.png" },
        { "title": "Portafolio Utilizando Tailwind css", "description": "Este Portafolio es para practicar Tailwind css utilizando vite y react", "in_progress": True, "image": "images/portafolio_tws.png" }
    ]

def proyectos(request):
    proyectos_activos = [p for p in projects if p["in_progress"]]
    return render(request, 'proyectos.html', {'projects': proyectos_activos})




def contacto(request):
    return render(request, 'contacto.html')
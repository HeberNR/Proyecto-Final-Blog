from django.shortcuts import render
from .models import Entrada


# Create your views here.

def inicio (request):
    return render (request, 'inicio.html', {})

def home(request):
    articulos = Entrada.objects.all()
    return render(request, "bienvenida.html", {"articulos": articulos})


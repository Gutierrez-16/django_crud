from django.shortcuts import render
from .models import Alumno

# Create your views here.

def inicio(request):
    alumnos = Alumno.objects.all()
    return render(request, 'Alumno/inicio.html', {'alumnos': alumnos})  
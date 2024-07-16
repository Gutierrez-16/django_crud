from django.db import OperationalError, transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Alumno
import time


def save_with_retry(instance, max_retries=5, delay=0.1):
    for attempt in range(max_retries):
        try:
            with transaction.atomic():
                instance.save()
            return
        except OperationalError:
            if attempt < max_retries - 1:
                time.sleep(delay)
            else:
                raise

def inicio(request):
    alumnos = Alumno.objects.all()
    context = {
        'alumnos': alumnos
    }
    return render(request, 'Alumno/inicio.html', context)

def crear_estudiante(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        edad = request.POST['edad']
        sexo = request.POST['sexo']
        nuevo_alumno = Alumno(nombre=nombre, edad=edad, sexo=sexo)
        save_with_retry(nuevo_alumno)
        return redirect(reverse('inicio'))
    return render(request, 'Alumno/inicio.html')

def editar_estudiante(request, id):
    alumno = get_object_or_404(Alumno, pk=id)
    if request.method == 'POST':
        alumno.nombre = request.POST['nombre']
        alumno.edad = request.POST['edad']
        alumno.sexo = request.POST['sexo']
        save_with_retry(alumno)
        return redirect(reverse('inicio'))
    context = {
        'alumno': alumno
    }
    return render(request, 'Alumno/inicio.html', context)

def eliminar_estudiante(request, id):
    alumno = get_object_or_404(Alumno, pk=id)
    if request.method == 'POST':
        alumno.delete()
        return redirect(reverse('inicio'))
    context = {
        'alumno': alumno
    }
    return render(request, 'Alumno/inicio.html', context)
    
    
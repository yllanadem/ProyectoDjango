from django.shortcuts import render
from django.http import HttpResponse
from AppDjango.models import *

# Create your views here.
def curso(self):
    curso=Curso(nombre="Python con Django", grupo="12345")
    curso.save()
    documento=f"Curso: {curso.nombre}  Grupo:{curso.grupo}"
    return HttpResponse(documento)
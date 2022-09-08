from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.

def curso(self):

    curso = Curso(nombre = "Desarrollo Web", camada = 12345)
    curso.save()

    respuesta = f'-> Curso: {curso.nombre} Camada: {curso.camada}'

    return HttpResponse(respuesta)

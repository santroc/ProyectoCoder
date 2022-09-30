from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length = 40)
    camada = models.IntegerField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Camada: {self.camada}'

class Estudiante(models.Model):

    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    email = models.EmailField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}'

class Profesor(models.Model):

    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    email = models.EmailField()
    profesion = models.CharField(max_length = 30)

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Profesión: {self.profesion}'

class Entregable(models.Model):

    nombre = models.CharField(max_length = 30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Fecha de entrega: {self.fechaDeEntrega} - Entregado: {self.entregado}'


class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta Avatares de media
    image = models.ImageField(upload_to='avatares', null = True, blank = True)


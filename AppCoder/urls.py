from django.urls import path
from AppCoder.views import inicio, cursos, profesores, entregables, estudiantes

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('cursos', cursos, name='Cursos'),
    path('profesores', profesores, name='Profesores'),
    path('estudiantes', estudiantes, name='Estudiantes'),
    path('entregables', entregables, name='Entregables'),

]
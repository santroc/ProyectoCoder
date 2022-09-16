from django.urls import path
from AppCoder.views import inicio, cursos, profesores, entregables, estudiantes, home, cursoFormulario, profesorFormulario, busquedaCamada, buscar, api_estudiantes, buscar_estudiante

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('cursos', cursos, name='Cursos'),
    path('profesores', profesores, name='Profesores'),
    path('estudiantes', estudiantes, name='Estudiantes'),
    path('entregables', entregables, name='Entregables'),
    path('home', home, name='home'),
    path('cursoFormulario', cursoFormulario, name = 'Curso formulario'),
    path('profesorFormulario', profesorFormulario, name = 'Profesor formulario'),
    path('busquedaCamada', busquedaCamada, name = 'BusquedaCamada'),
    path('buscar/', buscar),
    path('api_estudiantes', api_estudiantes),
    path('buscar_estudiante', buscar_estudiante)
]
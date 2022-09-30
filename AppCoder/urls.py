from re import template
from django.urls import path
from AppCoder.views import *#inicio, cursos, profesores, entregables, estudiantes, home, cursoFormulario, profesorFormulario, busquedaCamada, buscar, api_estudiantes, buscar_estudiante, create_estudiantes, delete_estudiantes, read_estudiantes, update_estudiantes
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('cursos', cursos, name='Cursos'),
    path('profesores', profesores, name='Profesores'),
    path('estudiantes', estudiantes, name='Estudiantes'),
    path('entregables', entregables, name='Entregables'),
    path('home', inicio, name='home'),
    path('cursoFormulario', cursoFormulario, name = 'Curso formulario'),
    path('profesorFormulario', profesorFormulario, name = 'Profesor formulario'),
    path('busquedaCamada', busquedaCamada, name = 'BusquedaCamada'),
    path('buscar/', buscar),
    path('api_estudiantes', api_estudiantes),
    path('buscar_estudiante', buscar_estudiante),
    path('create_estudiante', create_estudiantes, name = 'Create Estudiantes'),
    path('update_estudiante/<estudiante_id>', update_estudiantes, name = 'Update Estudiantes'),
    path('read_estudiante', read_estudiantes, name = 'Read Estudiantes'),
    path('delete_estudiante/<estudiante_id>', delete_estudiantes, name = 'Delete Estudiantes'),
#Usando el coso basado en vistas
    path('curso/list', CursoList.as_view(), name="List"),
    path(r'^(?P<pk>\d+)$', CursoDetalle.as_view(), name="Detail"),
    #path(r'^nuevo$', CursoCreacion.as_view(),name="New"),
    path(r'^editar/(?P<pk>\d+)$', CursoUpdate.as_view(),name="Edit"),
    path(r'^borrar/(?P<pk>\d+)$', CursoDelete.as_view(),name="Delete"),
    path('estudiante/list', EstudianteList.as_view(), name="List"),
    path(r'^nuevo$', EstudianteCreacion.as_view(),name="New_Student"),
    path('login/', login_request, name="Login"),
    path('register/', register, name="register"),
    path('logout/', LogoutView.as_view(template_name = 'inicio.html'), name="logout"),
    path('profile/editarPerfil', editarPerfil, name="editProfile"),
    path('profile/changepass', change_pass, name="change_pass"),
    path('profile/', profile, name="profile"),
    path('profile/changeAvatar', agregarAvatar, name ='changeAvatar')
]
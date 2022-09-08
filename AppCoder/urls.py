from django.urls import path
from AppCoder.views import inicio, cursos, profesores, entregables, estudiantes

urlpatterns = [
    path('', inicio),
    path('cursos', cursos),
    path('profesores', profesores),
    path('estudiantes', estudiantes),
    path('entregables', entregables),

]
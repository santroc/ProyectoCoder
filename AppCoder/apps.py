from django.apps import AppConfig


class AppcoderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppCoder'

def ready(self):

    from django.contrib import admin
    from AppCoder.models import Curso, Estudiante, Profesor, Entregable

    admin.site.register(Curso)
    admin.site.register(Estudiante)
    admin.site.register(Profesor)
    admin.site.register(Entregable)
from django.contrib import admin
from django.contrib import admin
from AppCoder.models import *

# Register your models here.

admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)

admin.site.register(Avatar)
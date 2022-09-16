from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso, Profesor, Estudiante
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario

# Create your views here.

# def curso(self):

#     curso = Curso(nombre = "Desarrollo Web", camada = 12345)
#     curso.save()

#     respuesta = f'-> Curso: {curso.nombre} Camada: {curso.camada}'

#     return HttpResponse(respuesta)

def inicio(request):

    return render(request, 'inicio.html')

def cursos(request):

    return render(request, 'cursos.html')

def profesores(request):

    return render(request, 'profesores.html')

def estudiantes(request):

    if(request.method == 'POST'):
        estudiante = Estudiante(nombre= request.POST['nombre'], 
                                apellido=request.POST['apellido'],
                                email=request.POST['email'])
        estudiante.save()
        return render(request, 'inicio.html')
    return render(request, 'estudiantes.html')

def api_estudiantes(request):

    if (request.method == "POST"):

        formulario = EstudianteFormulario(request.POST)

        if (formulario.is_valid()):
            informacion = formulario.cleaned_data
            estudiante = Estudiante(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'])
            estudiante.save()
            return render(request, 'api_estudiantes.html')
    else:
        formulario = EstudianteFormulario()
    return render(request, 'api_estudiantes.html', {'formulario': formulario, 'resultado': 'Success!'})

def buscar_estudiante(request):
    
    if (request.GET['email']):
        email = request.GET['email']
        estudiantes = Estudiante.objects.filter(email__icontains = email)

        return render(request, 'estudiantes.html', {"estudiantes": estudiantes})
    else:
        respuesta = f"No enviaste datos"
    return HttpResponse(respuesta)

def entregables(request):

    return render(request, 'entregables.html')

def home(request):

    return render(request, 'padre.html')

def cursoFormulario(request):

    if(request.method == 'POST'):

        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if(miFormulario.is_valid):

            informacion = miFormulario.cleaned_data

            curso = Profesor(nombre = informacion['curso'], camada = informacion['cursada'])
            curso.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = CursoFormulario() #Formulario vacío para contruir el HTML

    return render(request, 'cursoFormulario.html', {"miFormulario": miFormulario})

def profesorFormulario(request):
    if(request.method == 'POST'):

        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if(miFormulario.is_valid):

            informacion = miFormulario.cleaned_data

            profesor = Profesor(nombre = informacion['nombre'], apellido = informacion['apellido']
            ,email= informacion['email'], profesion= informacion['profesion'])
            profesor.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = ProfesorFormulario() #Formulario vacío para contruir el HTML

    return render(request, 'profesorFormulario.html', {"miFormulario": miFormulario})


def busquedaCamada(request):

    return render(request, 'busquedaCamada.html')

def buscar(request):

    if request.GET["camada"]:
        
        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains= camada)

        return render(request, 'resultadosBusqueda.html', {"cursos": cursos, "camada": camada})
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

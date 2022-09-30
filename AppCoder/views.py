from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso, Profesor, Estudiante, Avatar
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, UserRegistroForm, UserEditForm, ChangePasswordForm, AvatarFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

# Create your views here.

# def curso(self):

#     curso = Curso(nombre = "Desarrollo Web", camada = 12345)
#     curso.save()

#     respuesta = f'-> Curso: {curso.nombre} Camada: {curso.camada}'

#     return HttpResponse(respuesta)

@login_required
def inicio(request):

    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'inicio.html', {'avatar': avatar})

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
        avatar = Avatar.objects.filter(user = request.user.id)
        try:
            avatar = avatar[0].image.url
        except:
            avatar = None
        return render(request, 'inicio.html', {'avatar': avatar})
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
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'inicio.html', {'avatar': avatar})
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

            avatar = Avatar.objects.filter(user = request.user.id)

            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'inicio.html', {'avatar': avatar})
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


# Clase de CRUD y Views

def create_estudiantes(request):

    if request.method == 'POST':
        estudiante = Estudiante(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
        estudiante.save()
        estudiantes = Estudiante.objects.all()
        return render(request, 'read_estudiantes.html', {'estudiantes': estudiantes})
    return render(request, 'create_estudiantes.html')


def update_estudiantes(request, estudiante_id):
    estudiante = Estudiante.objects.get(id = estudiante_id)

    if (request.method == 'POST'):
        formulario = EstudianteFormulario(request.POST)
        if (formulario.is_valid()):
            informacion = formulario.cleaned_data
            estudiante.nombre = informacion['nombre']
            estudiante.apellido = informacion['apellido']
            estudiante.email = informacion['email']
            estudiante.save()
            estudiantes = Estudiante.objects.all()
            return render(request, 'read_estudiantes.html', {'estudiantes': estudiantes})
    else: 
        formulario = EstudianteFormulario(initial={'nombre': estudiante.nombre,
        'apellido': estudiante.apellido, 'email': estudiante.email})
    return render(request, 'update_estudiantes.html', {"formulario": formulario})

def read_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'read_estudiantes.html', {'estudiantes': estudiantes})

def delete_estudiantes(request, estudiante_id):
    estudiante = Estudiante.objects.get(id = estudiante_id)
    estudiante.delete()

    estudiantes = Estudiante.objects.all()
    return render(request, 'read_estudiantes.html', {'estudiantes': estudiantes})


#Clases basada en vistas

class CursoList(ListView):
    model = Curso
    template_name = "AppCoder/curso_list.html"

class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detalle.html"

# class CursoCreacion(CreateView):
#     model = Curso
#     success_url = "/AppCoder/curso/list"
#     fields = ["nombre", "camada"]

class CursoUpdate(UpdateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ["nombre", "camada"]

class CursoDelete(DeleteView):
    model = Curso
    success_url = "/AppCoder/curso/list"

class EstudianteCreacion(CreateView):
    model = Estudiante
    template_name = 'estudiante_formi.html'
    success_url = 'estudiante_list.html'
    fields = ['nombre', 'apellido', 'email']

class EstudianteList(ListView):
    model = Estudiante
    template_name = 'estudiante_list.html'


def login_request(request):
    
    if (request.method == 'POST'):
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username = user, password = pwd)

            if (user is not None):
                login(request, user)
                avatar = Avatar.objects.filter(user = request.user.id)
                try:
                    avatar = avatar[0].image.url
                except:
                    avatar = None
                return render(request, 'inicio.html', {'avatar': avatar})
            else:
                return render(request, "login.html", {'form': form})
        else:
            return render(request, "login.html", {'form': form})
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):

    if (request.method == 'POST'):
        #form = CreationForm(request, request.POST)
        form = UserRegistroForm(request.POST)
        if (form.is_valid()):
            #username = form.cleaned_data['username']
            form.save()
            return redirect('/AppCoder/login/')#render(request, 'login.html')
        else:#decidi regresar el formulario con error
            return render(request, "registro.html", {'form': form})
    form = UserRegistroForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if (request.method == 'POST'):
        form = UserEditForm(request.POST, instance = usuario)
        if(form.is_valid()):
            #Datos que se van a actualizar
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'inicio.html', {'avatar': avatar})
        else:
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'inicio.html', {'form': form,'avatar': avatar})
    else:
        form = UserEditForm(initial = {'email': usuario.email, 'username': usuario.username,
        'first_name': usuario.first_name, 'last_name': usuario.last_name})
    return render(request, 'editarPerfil.html', {'form': form, 'usuario': usuario})

@login_required
def change_pass(request):
    usuario = request.user
    if (request.method == 'POST'):
        form = ChangePasswordForm(data = request.POST, user = request.user)
        #form = PasswordChangeForm(date = request.POST, user = usuario)
        if (form.is_valid()):
            user = form.save()
            update_session_auth_hash(request, user)
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'inicio.html', {'avatar': avatar})
    else:
        #form = PasswordChangeForm(request.user)
        form = ChangePasswordForm(user = request.user)

    return render(request, 'changepass.html', {'form': form, 'usuario': usuario})

@login_required
def profile(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'profile.html', {'avatar': avatar})

def agregarAvatar(request):

    if(request.method == 'POST'):
        form = AvatarFormulario(request.POST, request.FILES)
        if(form.is_valid()):
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'inicio.html', {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarFormulario()
        except:
            form = AvatarFormulario()
    return render(request, 'AgregarAvatar.html', {'form': form})




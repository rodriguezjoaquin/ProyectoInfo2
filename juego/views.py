from django.shortcuts import render, redirect

from .forms import PreguntaForm
from .models import Pregunta, Respuesta, Partida
from datetime import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def listar_preguntas(request):
     if request.method == "POST":
        resultado = 0
        for i in range(1,4):
            opcion = Respuesta.objects.get(pk=request.POST[str(i)])
            resultado += opcion.puntaje
        Partida.objects.create(usuario=request.user, fecha=datetime.now, resultado= resultado)
        return redirect("/")
     else:
        data = {}
        preguntas = Pregunta.objects.all().order_by('?')[:3]
        for item in preguntas:
            respuestas = Respuesta.objects.filter(id_pregunta=item.id)
            data[item.pregunta]= respuestas

        return render(request, 'juego/listar_preguntas.html', {"preguntas":data})


def preguntas(request):
    preguntas= Pregunta.objects.all()
    return render(request, 'juego/preguntas.html', {"pregunta": preguntas})

def detalle_pregunta(request, identificador):
    pregunta = Pregunta.objects.get(pk=identificador)
    return render(request, 'juego/detalle_pregunta.html', {"pregunta": pregunta})

def crear_pregunta(request):
    form = PreguntaForm()
    if request.method == "POST":
        form = PreguntaForm(request.POST)
    if form.is_valid():
            registro = form.save(commit=False)
            registro.autor = request.user
            registro.fecha_creacion = datetime.now()
            registro.save()
    return render(request, 'juego/crear_pregunta.html', {'form': form})

def editar_pregunta(request, identificador):
    pregunta= Pregunta.objects.get(pk=identificador)
    if request.method == "POST":
        form = PreguntaForm(request.POST, instance=pregunta)
        if form.is_valid():
            item = form.save(commit=False)
            item.autor = request.user
            item.fecha_creacion = datetime.now()
            item.save()
            return redirect('juego:detalle_pregunta', identificador=item.id)
    else:
        form = PreguntaForm(instance=pregunta)
    return render(request, 'juego/editar_pregunta.html', {'form': form})

def eliminar_pregunta(request, identificador):
    pregunta = Pregunta.objects.get(pk=identificador)
    return render(request, 'juego/eliminar_pregunta.html', {"pregunta": pregunta})

def confirmar_eliminacion(request, identificador):
    Pregunta.objects.get(pk=identificador).delete()
    return redirect("/")

def crear_pregunta(request):
    if request.user.has_perm('juego.add_pregunta'):
        if request.method == "POST":
            form = PreguntaForm(request.POST)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.fecha_creacion = datetime.now()
                registro.save()
        form = PreguntaForm()
        return render(request, 'juego/crear_pregunta.html', {'form': form})
    else:
        return redirect("/")

from django.contrib.auth.decorators import permission_required
@login_required(login_url='/login')
@permission_required('juedo.add_pregunta', login_url='/login')
def crear_pregunta(request):
    form = PreguntaForm()
    if request.method == "POST":
        form = PreguntaForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.autor = request.user
            registro.fecha_creacion = datetime.now()
            registro.save()
            return redirect('juego:preguntas')
    return render(request, 'juego/crear_pregunta.html', {'form': form})




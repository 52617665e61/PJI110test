from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template import loader
from .models import Perdido, Encontrado
from .forms import PerdidoForm, EncontradoForm
from django.contrib.auth.models import User



# Create your views here.


def index(request):
    return render(request, 'tasks/index.html')

##########################################################################################################################


#VIEWS REFERENTES A ANIMAIS ENCONTRADOS


##########################################################################################################################

def listaEncontrados(request):
     encontrados = Encontrado.objects.all()
     return render(request, 'tasks/listaEncontrados.html', {'encontrados': encontrados})


def encontrado(request):
    return render(request, 'tasks/encontrado.html')

@login_required
def addEncontrado(request):
    if request.method == 'POST':
        form = EncontradoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EncontradoForm()
        return render(request, 'tasks/addEncontrado.html', {'form': form})
    
##########################################################################################################################


#VIEwS REFERENTES A ANIMAIS PERDIDOS 
    

##########################################################################################################################    
def perdido(request):
    return render(request, 'tasks/perdido.html')

@login_required
def addPerdido(request):
    if request.method == 'POST':
        form = PerdidoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.usuario = '1'
            form.save()
            return redirect('/')
    else:
        form = PerdidoForm()
        return render(request, 'tasks/addPerdido.html', {'form': form})

def listaPerdidos(request):
     
     perdidos = Perdido.objects.all()
     return render(request, 'tasks/listaPerdidos.html', {'perdidos': perdidos})

##########################################################################################################################


#VIEWS INFORMAÇÕES SOBRE OS ANIMAIS


##########################################################################################################################

def informacoes(request, id):
    info = Perdido.objects.all().filter(id=id)
    return render(request, 'tasks/informacoes.html', {'info': info})
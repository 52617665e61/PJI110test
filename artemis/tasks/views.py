from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AnimaisRegistrados
from .forms import AnimaisRegistroForm




# Create your views here.


def index(request):
    return render(request, 'tasks/index.html')


##########################################################################################################################


#VIEWS REFERENTES A ANIMAIS ENCONTRADOS


##########################################################################################################################

def listaEncontrados(request):
     encontrados = AnimaisRegistrados.objects.all().order_by('-id').filter(tipoRegistro='Encontrado')
     return render(request, 'tasks/listaEncontrados.html', {'encontrados': encontrados})


def encontrado(request):
    return render(request, 'tasks/encontrado.html')

@login_required
def addEncontrado(request):
    if request.method == 'POST':
        form = AnimaisRegistroForm(request.POST, request.FILES)
        if form.is_valid():
            processo = form.save(commit=False)
            processo.usuario = request.user.id
            processo.tipoRegistro = 'Encontrado'
            processo.save()
            return redirect('perfil')
    else:
        form = AnimaisRegistroForm()
        return render(request, 'tasks/addEncontrado.html', {'form': form})
    
##########################################################################################################################


#VIEwS REFERENTES A ANIMAIS PERDIDOS 
    

##########################################################################################################################    
def perdido(request):
    return render(request, 'tasks/perdido.html')

@login_required
def addPerdido(request):
    if request.method == 'POST':
        form =AnimaisRegistroForm(request.POST, request.FILES)
        if form.is_valid():
            processo = form.save(commit=False)
            processo.usuario = request.user.id
            processo.tipoRegistro = 'Perdido'
            processo.save()
            return redirect('perfil')
    else:
        form = AnimaisRegistroForm()
        return render(request, 'tasks/addPerdido.html', {'form': form})

def listaPerdidos(request):
     
     perdidos = AnimaisRegistrados.objects.all().order_by('-id').filter(tipoRegistro='Perdido')
     return render(request, 'tasks/listaPerdidos.html', {'perdidos': perdidos})

##########################################################################################################################


#VIEWS INFORMAÇÕES SOBRE OS ANIMAIS


##########################################################################################################################

def informacoes(request, id):
    info = AnimaisRegistrados.objects.all().filter(id=id)
    return render(request, 'tasks/informacoes.html', {'info': info})

@login_required
def editarRegistro(request, id):
    registro = AnimaisRegistrados.objects.get(id=id)
    form = AnimaisRegistroForm(request.POST or None, request.FILES or None,instance=registro)
    if form.is_valid():
        form.save()
        return redirect('perfil')
    return render(request, 'tasks/editarRegistro.html', {'registro': registro, 
                                                         'form':form})


@login_required
def deletaRegistro(request, id):
    registro = AnimaisRegistrados.objects.get(id=id)
    registro.delete()
    return redirect('perfil')
    
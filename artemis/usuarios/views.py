from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import formularioRegistroUsuario


##########################################################################################################################

# REGISTRO DE USUÁRIOS

##########################################################################################################################

def registroUsuario(request):
    if request.method=="POST":
        form = formularioRegistroUsuario(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data['username']
            senha = form.cleaned_data['password1']
            user = authenticate(username=usuario, password=senha)
            login(request, user)
            return redirect('home')
    else:
        form = formularioRegistroUsuario()


    return render(request, 'registration/registroUsuario.html',{'form':form})


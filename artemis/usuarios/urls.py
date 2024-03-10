from django.urls import path, include
from . import views

urlpatterns=[
    path('registroUsuario', views.registroUsuario, name='registroUsuario'),
]
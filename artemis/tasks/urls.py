from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #PATH ENCONTRADOS
    path('listaEncontrados', views.listaEncontrados, name='listaEncontrados'),
    path('encontrado', views.encontrado, name='encontrado'),
    path('addEncontrado', views.addEncontrado, name='addEncontrado'),
    #PATH PERDIDOS
    path('perdido', views.perdido, name= 'perdido'),
    path('addPerdido', views.addPerdido, name='addPerdido'),    
    path('listaPerdidos', views.listaPerdidos, name='listaPerdidos'),
    path('informacoes/<int:id>', views.informacoes, name='informacoes'),
    path('informacoes/editarRegistro/<int:id>', views.editarRegistro, name='editarRegistro'),
    path('deletaRegistro<int:id>', views.deletaRegistro, name='deletaRegistro')
]
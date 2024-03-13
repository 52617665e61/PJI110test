from django import forms
from .models import Perdido, Encontrado
from django.contrib.admin.widgets import AdminDateWidget

class PerdidoForm(forms.ModelForm):
    class Meta:
        model = Perdido
        fields = ('especie', 'raca', 'cor', 'tamanho', 'tempo', 'contato','img', 'adicional','usuario')
        widgets = {
            'tempo': forms.TextInput(attrs={'placeholder':'dd/mm/yyyy'}),
            'usuario':forms.HiddenInput()
        }
        labels = {
            'especie': 'Espécie do animal perdido',
            'raca': 'Raça',
            'tamanho' :'Porte',
            'localidade' :'Último local visto',
            'tempo' : 'Último dia visto',
            'img' : 'Adicione uma imagem do animal perdido'
        }

class EncontradoForm(forms.ModelForm):
   class Meta:
        model = Encontrado
        fields = ('especie', 'raca', 'cor', 'tamanho', 'tempo', 'contato','img', 'adicional','fk')
        widgets = {
            'tempo': forms.TextInput(attrs={'placeholder':'dd/mm/yyyy'}),
        }
        labels = {
            'especie': 'Espécie do animal perdido',
            'raca': 'Raça',
            'tamanho' :'Porte',
            'localidade' :'Último local visto',
            'tempo' : 'Último dia visto',
            'img' : 'Adicione uma imagem do animal perdido'
        }
   ''' class Meta:
        model = Encontrado
        fields = ('especie', 'raca', 'cor', 'tamanho', 'localidade', 'caracteristica', 'tempo', 'contato', 'img')'''

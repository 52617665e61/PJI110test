from django import forms
from .models import AnimaisRegistrados
from django.contrib.admin.widgets import AdminDateWidget

class AnimaisRegistroForm(forms.ModelForm):
    class Meta:
        model = AnimaisRegistrados
        fields = ('nome','especie', 'raca', 'cor', 'tamanho', 'tempo', 'contato','img', 'adicional')
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder' : 'Se não souber o nome coloque a espécie. Exemplo: Cachorro, Gato, etc.'}),
            'tempo': forms.TextInput(attrs={'placeholder':'dd/mm/yyyy'})
        }
        labels = {
            'especie': 'Espécie do animal perdido',
            'raca': 'Raça',
            'tamanho' :'Porte',
            'localidade' :'Último local visto',
            'tempo' : 'Último dia visto',
            'img' : 'Adicione uma imagem do animal perdido'
        }


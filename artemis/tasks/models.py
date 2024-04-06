from django.db import models
from django.conf import settings
from django.utils import dateformat
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User




##########################################################################################################################

#CONFIGURAÇÕES DOS CHOICES

##########################################################################################################################

especie = (
    ('Cachorro', 'cachorro'),
    ('Cavalo', 'cavalo'),
    ('Gato', 'gato'),
    ('Periquito', 'periquito')
    
    
)
cachorro =(('Shih-Tzu', 'Shih-Tzu'),
    ('Buldogue Francês', 'Buldogue Francês'),)
raca = (
    ('Shih-Tzu', 'Shih-Tzu'),
    ('Buldogue Francês', 'Buldogue Francês'),
    ('Yorkshire Terrier','Yorkshire Terrier'),
    ('Poodle','Poodle'),
    ('Maltês','Maltês'),
    ('Pug','Pug'),
    ('Sem raça definida','SRD')
)

cor = (
    ('Amarelo', 'Amarelo'),
    ('Azul', 'Azul'),
    ('Branco', 'Branco'),
    ('Marrom', 'Marrom'),
    ('Preto', 'Preto')
)

tamanho = (
    ('Pequeno', 'pequeno'),
    ('M', 'medio'),
    ('G', 'grande')
)

##########################################################################################################################



class Perdido(models.Model):
    nome = models.CharField('Nome do animal', max_length=20, default='Pet')
    id = models.IntegerField(primary_key=True)
    especie = models.CharField(max_length=20, choices = especie)
    raca = models.CharField(max_length=20, choices = raca)
    cor = models.CharField(max_length=20, choices=cor)
    tamanho = models.CharField(max_length=20, choices = tamanho)
    localidade = models.CharField(max_length=20)
    tempo = models.DateField()
    contato = models.CharField(max_length=20)
    img = models.ImageField(null=True,blank=True, upload_to='animais/')
    adicional = models.CharField('Informações adicionais', null=True, max_length=300)
    usuario = models.IntegerField()
    
    def __str__(self):
        return self.nome

class Encontrado(models.Model):
    id = models.IntegerField(primary_key=True)
    fk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    especie = models.CharField(max_length=20, choices = especie)
    raca = models.CharField(max_length=20, choices = raca)
    cor = models.CharField(max_length=20, choices=cor)
    tamanho = models.CharField(max_length=20, choices = tamanho)
    localidade = models.CharField(max_length=20)
    tempo = models.DateField()
    contato = models.CharField(max_length=20)
    img = models.ImageField(null=True,blank=True, upload_to='animais/')
    adicional = models.CharField('Informações adicionais', null=True, max_length=300)

    def __str__(self):
        return "{},{}".format(self.especie, self.raca)

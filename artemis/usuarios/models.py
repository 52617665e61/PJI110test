from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, default=User.username)
    primeiroNome = models.CharField(max_length=14, null=True)
    ultimoNome=models.CharField(max_length=14, null=True)
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
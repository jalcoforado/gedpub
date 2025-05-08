from django.db import models
from django.contrib.auth.models import AbstractUser

class Secretaria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Setor(models.Model):
    nome = models.CharField(max_length=100)
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.secretaria.nome}"

class Usuario(AbstractUser):
    setor = models.ForeignKey(Setor, null=True, blank=True, on_delete=models.SET_NULL)
    cargo = models.CharField(max_length=100, blank=True)
    ativo = models.BooleanField(default=True)

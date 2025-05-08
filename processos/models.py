from django.db import models
from usuarios.models import Setor, Usuario
from django.utils.timezone import now

# Create your models here.
class Processo(models.Model):
    numero = models.CharField(max_length=30, unique=True)
    tipo = models.CharField(max_length=100)
    assunto = models.TextField()
    setor_origem = models.ForeignKey(Setor, related_name='origem', on_delete=models.CASCADE)
    criado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    criado_em = models.DateTimeField(default=now)
    status = models.CharField(max_length=50, default='Em aberto')

class Tramite(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    setor_origem = models.ForeignKey(Setor, related_name='tramites_origem', on_delete=models.CASCADE)
    setor_destino = models.ForeignKey(Setor, related_name='tramites_destino', on_delete=models.CASCADE)
    despacho = models.TextField()
    enviado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    enviado_em = models.DateTimeField(default=now)

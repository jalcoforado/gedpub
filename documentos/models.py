from django.db import models
from processos.models import Processo
from usuarios.models import Usuario
from django.utils.timezone import now

class Documento(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE, related_name='documentos')
    nome = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to='documentos/')
    versao = models.IntegerField(default=1)
    criado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    criado_em = models.DateTimeField(default=now)

    class Meta:
        unique_together = ('processo', 'nome', 'versao')

    def __str__(self):
        return f"{self.nome} v{self.versao}"

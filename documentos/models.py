from django.db import models
from django.contrib.auth.models import User

class Setor(models.Model):
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    senha = models.CharField(max_length=255)
    setor = models.ForeignKey(Setor, on_delete=models.SET_NULL, null=True)
    is_ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

class GrupoPermissao(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

class UsuarioGrupo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    grupo = models.ForeignKey(GrupoPermissao, on_delete=models.CASCADE)

class TipoDocumento(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

class StatusDocumento(models.Model):
    nome = models.CharField(max_length=255)
    cor = models.CharField(max_length=20)

class TipoProcesso(models.Model):
    nome = models.CharField(max_length=255)

class StatusProcesso(models.Model):
    nome = models.CharField(max_length=255)

class Assunto(models.Model):
    descricao = models.TextField()

class Processo(models.Model):
    numero_processo = models.CharField(max_length=100)
    assunto = models.ForeignKey(Assunto, on_delete=models.SET_NULL, null=True)
    tipo_processo = models.ForeignKey(TipoProcesso, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(StatusProcesso, on_delete=models.SET_NULL, null=True)
    criado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

class Documento(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(StatusDocumento, on_delete=models.SET_NULL, null=True)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    caminho_arquivo = models.CharField(max_length=500)
    versao_atual = models.IntegerField()

class VersaoDocumento(models.Model):
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)
    numero_versao = models.IntegerField()
    criado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    caminho_arquivo = models.CharField(max_length=500)

class AssinaturaDigital(models.Model):
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    certificado_digital = models.TextField()
    data_assinatura = models.DateTimeField()
    tipo_assinatura = models.CharField(max_length=50)

class Movimento(models.Model):
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)
    de_setor = models.ForeignKey(Setor, on_delete=models.SET_NULL, null=True, related_name='movimentos_saida')
    para_setor = models.ForeignKey(Setor, on_delete=models.SET_NULL, null=True, related_name='movimentos_entrada')
    usuario_responsavel = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    data_envio = models.DateTimeField()
    data_recebimento = models.DateTimeField(null=True, blank=True)
    observacao = models.TextField()

class CaixaEntrada(models.Model):
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    data_entrada = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField(default=False)

class Notificacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensagem = models.TextField()
    lida = models.BooleanField(default=False)
    tipo = models.CharField(max_length=50)
    data_envio = models.DateTimeField(auto_now_add=True)

class PermissaoSetorDocumento(models.Model):
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    pode_criar = models.BooleanField(default=False)
    pode_visualizar = models.BooleanField(default=False)
    pode_editar = models.BooleanField(default=False)
    pode_assinar = models.BooleanField(default=False)

class LogSistema(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    acao = models.TextField()
    objeto_afetado = models.CharField(max_length=255)
    objeto_id = models.IntegerField()
    data_hora = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()

class FluxoPredefinido(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

class EtapaFluxo(models.Model):
    fluxo = models.ForeignKey(FluxoPredefinido, on_delete=models.CASCADE)
    ordem = models.IntegerField()
    setor = models.ForeignKey(Setor, on_delete=models.SET_NULL, null=True)
    acao_esperada = models.CharField(max_length=255)

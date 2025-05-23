from django.db import models
from rest_framework import serializers
from .models import Setor, Usuario, GrupoPermissao, UsuarioGrupo, TipoDocumento, \
    StatusDocumento, TipoProcesso, StatusProcesso, Assunto, Processo, Documento, \
    VersaoDocumento, AssinaturaDigital, Movimento, CaixaEntrada, Notificacao, \
    PermissaoSetorDocumento, LogSistema, FluxoPredefinido, EtapaFluxo
# SERIALIZERS

class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class GrupoPermissaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoPermissao
        fields = '__all__'

class UsuarioGrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioGrupo
        fields = '__all__'

class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'

class StatusDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusDocumento
        fields = '__all__'

class TipoProcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProcesso
        fields = '__all__'

class StatusProcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusProcesso
        fields = '__all__'

class AssuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assunto
        fields = '__all__'

class ProcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processo
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'

class VersaoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VersaoDocumento
        fields = '__all__'

class AssinaturaDigitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssinaturaDigital
        fields = '__all__'

class MovimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimento
        fields = '__all__'

class CaixaEntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaixaEntrada
        fields = '__all__'

class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = '__all__'

class PermissaoSetorDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissaoSetorDocumento
        fields = '__all__'

class LogSistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogSistema
        fields = '__all__'

class FluxoPredefinidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FluxoPredefinido
        fields = '__all__'

class EtapaFluxoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtapaFluxo
        fields = '__all__'

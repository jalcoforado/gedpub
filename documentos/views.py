from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    Setor, Usuario, GrupoPermissao, UsuarioGrupo, TipoDocumento, StatusDocumento,
    TipoProcesso, StatusProcesso, Assunto, Processo, Documento, VersaoDocumento,
    AssinaturaDigital, Movimento, CaixaEntrada, Notificacao, PermissaoSetorDocumento,
    LogSistema, FluxoPredefinido, EtapaFluxo
)
from .serializers import *

class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer
    permission_classes = [IsAuthenticated]

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class GrupoPermissaoViewSet(viewsets.ModelViewSet):
    queryset = GrupoPermissao.objects.all()
    serializer_class = GrupoPermissaoSerializer
    permission_classes = [IsAuthenticated]

class UsuarioGrupoViewSet(viewsets.ModelViewSet):
    queryset = UsuarioGrupo.objects.all()
    serializer_class = UsuarioGrupoSerializer
    permission_classes = [IsAuthenticated]

class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer
    permission_classes = [IsAuthenticated]

class StatusDocumentoViewSet(viewsets.ModelViewSet):
    queryset = StatusDocumento.objects.all()
    serializer_class = StatusDocumentoSerializer
    permission_classes = [IsAuthenticated]

class TipoProcessoViewSet(viewsets.ModelViewSet):
    queryset = TipoProcesso.objects.all()
    serializer_class = TipoProcessoSerializer
    permission_classes = [IsAuthenticated]

class StatusProcessoViewSet(viewsets.ModelViewSet):
    queryset = StatusProcesso.objects.all()
    serializer_class = StatusProcessoSerializer
    permission_classes = [IsAuthenticated]

class AssuntoViewSet(viewsets.ModelViewSet):
    queryset = Assunto.objects.all()
    serializer_class = AssuntoSerializer
    permission_classes = [IsAuthenticated]

class ProcessoViewSet(viewsets.ModelViewSet):
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer
    permission_classes = [IsAuthenticated]

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    permission_classes = [IsAuthenticated]

class VersaoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = VersaoDocumento.objects.all()
    serializer_class = VersaoDocumentoSerializer
    permission_classes = [IsAuthenticated]

class AssinaturaDigitalViewSet(viewsets.ModelViewSet):
    queryset = AssinaturaDigital.objects.all()
    serializer_class = AssinaturaDigitalSerializer
    permission_classes = [IsAuthenticated]

class MovimentoViewSet(viewsets.ModelViewSet):
    queryset = Movimento.objects.all()
    serializer_class = MovimentoSerializer
    permission_classes = [IsAuthenticated]

class CaixaEntradaViewSet(viewsets.ModelViewSet):
    queryset = CaixaEntrada.objects.all()
    serializer_class = CaixaEntradaSerializer
    permission_classes = [IsAuthenticated]

class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer
    permission_classes = [IsAuthenticated]

class PermissaoSetorDocumentoViewSet(viewsets.ModelViewSet):
    queryset = PermissaoSetorDocumento.objects.all()
    serializer_class = PermissaoSetorDocumentoSerializer
    permission_classes = [IsAuthenticated]

class LogSistemaViewSet(viewsets.ModelViewSet):
    queryset = LogSistema.objects.all()
    serializer_class = LogSistemaSerializer
    permission_classes = [IsAuthenticated]

class FluxoPredefinidoViewSet(viewsets.ModelViewSet):
    queryset = FluxoPredefinido.objects.all()
    serializer_class = FluxoPredefinidoSerializer
    permission_classes = [IsAuthenticated]

class EtapaFluxoViewSet(viewsets.ModelViewSet):
    queryset = EtapaFluxo.objects.all()
    serializer_class = EtapaFluxoSerializer
    permission_classes = [IsAuthenticated]

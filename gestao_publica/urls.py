from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from documentos.views import (
    DocumentoViewSet, SetorViewSet, UsuarioViewSet, GrupoPermissaoViewSet,
    UsuarioGrupoViewSet, TipoDocumentoViewSet, StatusDocumentoViewSet,
    TipoProcessoViewSet, StatusProcessoViewSet, AssuntoViewSet, ProcessoViewSet,
    VersaoDocumentoViewSet, AssinaturaDigitalViewSet, MovimentoViewSet,
    CaixaEntradaViewSet, NotificacaoViewSet, PermissaoSetorDocumentoViewSet,
    LogSistemaViewSet, FluxoPredefinidoViewSet, EtapaFluxoViewSet
)

# Roteador DRF
router = DefaultRouter()
router.register(r'documentos', DocumentoViewSet)
router.register(r'setor', SetorViewSet)
router.register(r'usuario', UsuarioViewSet)
router.register(r'grupo-permissao', GrupoPermissaoViewSet)
router.register(r'usuario-grupo', UsuarioGrupoViewSet)
router.register(r'tipo-documento', TipoDocumentoViewSet)
router.register(r'status-documento', StatusDocumentoViewSet)
router.register(r'tipo-processo', TipoProcessoViewSet)
router.register(r'status-processo', StatusProcessoViewSet)
router.register(r'assunto', AssuntoViewSet)
router.register(r'processo', ProcessoViewSet)
router.register(r'versao-documento', VersaoDocumentoViewSet)
router.register(r'assinatura-digital', AssinaturaDigitalViewSet)
router.register(r'movimento', MovimentoViewSet)
router.register(r'caixa-entrada', CaixaEntradaViewSet)
router.register(r'notificacao', NotificacaoViewSet)
router.register(r'permissao-setor-documento', PermissaoSetorDocumentoViewSet)
router.register(r'log', LogSistemaViewSet)
router.register(r'fluxo', FluxoPredefinidoViewSet)
router.register(r'etapa-fluxo', EtapaFluxoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Todas as rotas da API incluídas
]

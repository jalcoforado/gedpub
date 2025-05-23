from django.urls import path, include
from rest_framework.routers import DefaultRouter
from documentos.views import DocumentoViewSet
from .views import (
    SetorViewSet, UsuarioViewSet, GrupoPermissaoViewSet, UsuarioGrupoViewSet,
    TipoDocumentoViewSet, StatusDocumentoViewSet, TipoProcessoViewSet, StatusProcessoViewSet,
    AssuntoViewSet, ProcessoViewSet, DocumentoViewSet, VersaoDocumentoViewSet,
    AssinaturaDigitalViewSet, MovimentoViewSet, CaixaEntradaViewSet, NotificacaoViewSet,
    PermissaoSetorDocumentoViewSet, LogSistemaViewSet, FluxoPredefinidoViewSet, EtapaFluxoViewSet
)



router = DefaultRouter()
router.register(r'setores', SetorViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'grupos-permissao', GrupoPermissaoViewSet)
router.register(r'usuarios-grupo', UsuarioGrupoViewSet)
router.register(r'tipos-documento', TipoDocumentoViewSet)
router.register(r'status-documento', StatusDocumentoViewSet)
router.register(r'tipos-processo', TipoProcessoViewSet)
router.register(r'status-processo', StatusProcessoViewSet)
router.register(r'assuntos', AssuntoViewSet)
router.register(r'processos', ProcessoViewSet)
router.register(r'documentos', DocumentoViewSet)
router.register(r'versoes-documento', VersaoDocumentoViewSet)
router.register(r'assinaturas', AssinaturaDigitalViewSet)
router.register(r'movimentos', MovimentoViewSet)
router.register(r'caixa-entrada', CaixaEntradaViewSet)
router.register(r'notificacoes', NotificacaoViewSet)
router.register(r'permissoes-setor-documento', PermissaoSetorDocumentoViewSet)
router.register(r'logs', LogSistemaViewSet)
router.register(r'fluxos', FluxoPredefinidoViewSet)
router.register(r'etapas-fluxo', EtapaFluxoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Isso adiciona as URLs da API
]



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProcessoViewSet, TramiteViewSet, lista_processos
from .views import novo_processo, detalhe_processo

router = DefaultRouter()
router.register(r'processos', ProcessoViewSet)
router.register(r'tramites', TramiteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('lista/', lista_processos, name='lista_processos'),
    path('novo/', novo_processo, name='novo_processo'),
    path('<int:pk>/', detalhe_processo, name='detalhe_processo'),

]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import home  # <- importa a view
from django.conf.urls.static import static

urlpatterns = [
    path('', home),  # <- define a rota /
    path('admin/', admin.site.urls),
    path('api/', include('processos.urls')),
    path('api/documentos/', include('documentos.urls')),
    path('processos/', include('processos.urls')),


]



# Para servir arquivos de upload em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
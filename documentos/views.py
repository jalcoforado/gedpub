from rest_framework import viewsets
from .models import Documento
from .serializers import DocumentoSerializer

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all().order_by('-criado_em')
    serializer_class = DocumentoSerializer

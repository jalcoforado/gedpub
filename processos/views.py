from rest_framework import viewsets
from .models import Processo, Tramite
from .serializers import ProcessoSerializer, TramiteSerializer
from django.shortcuts import render
from .forms import ProcessoForm
from django.shortcuts import redirect
class ProcessoViewSet(viewsets.ModelViewSet):
    queryset = Processo.objects.all().order_by('-criado_em')
    serializer_class = ProcessoSerializer

class TramiteViewSet(viewsets.ModelViewSet):
    queryset = Tramite.objects.all().order_by('-enviado_em')
    serializer_class = TramiteSerializer

def lista_processos(request):
    processos = Processo.objects.all().order_by('-criado_em')
    return render(request, 'processos/lista.html', {'processos': processos})


def novo_processo(request):
    if request.method == 'POST':
        form = ProcessoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_processos')
    else:
        form = ProcessoForm()
    return render(request, 'processos/novo.html', {'form': form})


def detalhe_processo(request, pk):
    processo = get_object_or_404(Processo, pk=pk)
    tramites = Tramite.objects.filter(processo=processo).order_by('-data')
    return render(request, 'processos/detalhe.html', {
        'processo': processo,
        'tramites': tramites,
    })
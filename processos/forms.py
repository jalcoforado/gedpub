from django import forms
from .models import Processo

class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processo
        fields = ['numero', 'tipo', 'assunto', 'setor_origem', 'status']
        widgets = {
            'assunto': forms.Textarea(attrs={'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

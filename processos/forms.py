from django import forms
from django.forms import ModelForm

from .models import Processo, faseProcesso


class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processo

        fields = '__all__'


class faseProcessoForm(forms.ModelForm):
    class Meta:
        model = faseProcesso
        fields = '__all__'
        
class BuscaProcessosForm(forms.Form):
    
        nro_processo = forms.CharField(max_length=45)
        labels = {
        "nro_processo": "Número do Processo",
        }

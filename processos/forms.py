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

        fields = ["tipo_fase_processo", "desc", "processo"]

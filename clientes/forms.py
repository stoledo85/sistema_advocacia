from django import forms
from django.forms import ModelForm

from .models import Cliente


class CriarCliente(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'


class BuscaClienteForm(forms.Form):
    nome_cliente = forms.CharField(max_length=45)
    cpf = forms.CharField(max_length=11)
    labels = {
        "nome_cliente": "Nome",
        "cpf": "CPF",
    }

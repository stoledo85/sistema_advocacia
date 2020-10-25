from django import forms
from django.forms import ModelForm

from .models import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ["nome_cliente", "cpf", "rg", "estado_civil", "data_nascimento", "endereco",
                  "nro_endereco", "bairro", "cidade", "estado", "cep", "email", "telefone"]


class BuscaClienteForm(forms.Form):
    nome_cliente = forms.CharField(max_length=45)
    cpf = forms.CharField(max_length=11)
    labels = {
        "nome_cliente": "Nome",
        "cpf": "CPF",
    }

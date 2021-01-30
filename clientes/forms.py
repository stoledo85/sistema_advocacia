from django import forms
from django.forms import ModelForm

from .models import Cliente


class ClienteForm(ModelForm):
    """Formulário do cadastro do Cliente."""

    class Meta:
        model = Cliente
        fields = "__all__"
        labels = {
            "nome_cliente": "Nome Completo",
            "cpf": "CPF",
            "rg": "RG",
            "estado_civil": "Estado Civil",
            "data_nascimento": "Data de Nascimento",
            "endereco": "Endereço",
            "nro_endereco": "Número",
            "bairro": "Bairro",
            "cidade": "Cidade",
            "estado": "Estado",
            "cep": "CEP",
            "email": "E-mail",
            "telefone": "Telefone",
        }


class BuscaClienteForm(forms.Form):
    """
    Pesquisa o nome ou cpf do Cliente dentro de uma lista.
    Args:
        nome_cliente -- recebe uma string de tamanho 15 do nome.
        cpf -- recebe o nome do cpf sem pontos ou marcações.
    """

    nome_cliente = forms.CharField(max_length=45)
    cpf = forms.CharField(max_length=11)
    labels = {
        "nome_cliente": "Nome",
        "cpf": "CPF",
    }

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
        widgets = {
            "nome_cliente": forms.TextInput(attrs={"placeholder": "Ex: João da Silva"}),
            "cpf": forms.TextInput(attrs={"placeholder": "000.000.000-00"}),
            "rg": forms.TextInput(attrs={"placeholder": "00.000.000-0"}),
            "data_nascimento": forms.DateInput(attrs={"type": "date"}),
            "endereco": forms.TextInput(attrs={"placeholder": "Rua, Avenida, etc."}),
            "nro_endereco": forms.TextInput(attrs={"placeholder": "123"}),
            "cep": forms.TextInput(attrs={"placeholder": "00000-000"}),
            "email": forms.EmailInput(attrs={"placeholder": "email@exemplo.com"}),
            "telefone": forms.TextInput(attrs={"placeholder": "(00) 00000-0000"}),
            "bairro": forms.TextInput(attrs={"placeholder": "Bairro"}),
            "cidade": forms.TextInput(attrs={"placeholder": "Cidade"}),
        }


class BuscaClienteForm(forms.Form):
    nome_cliente = forms.CharField(
        max_length=45, 
        label="Nome do Cliente", 
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Pesquisar por nome..."})
    )
    cpf = forms.CharField(
        max_length=11, 
        label="CPF", 
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "000.000.000-00"})
    )

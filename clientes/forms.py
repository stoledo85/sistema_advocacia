from django import forms
from django.forms import ModelForm

from .models import Cliente, Endereco

class EnderecoForm(forms.ModelForm):

    class Meta:
        model = Endereco
        fields = ["logradouro_endereco", "nro_endereco",
                  "nome_bairro", "cidade_endereco", "cep"]
        help_texts = {
            "logradouro_endereco": "Nome da Rua",
            "nro_endereco": "Número do Imóvel",
            "nome_bairro": "Informar o Bairro da sua localidade"
        }
        labels = {
            "logradouro_endereco": "Endereço",
            "nro_endereco": "Número",
            "nome_bairro": "Bairro",
            "cidade_endereco": "Cidade", "cep": "CEP"
        }


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ["nome_cliente", "ctps_cliente", "profissao_cliente", "cpf", "rg", "nacionalidade",
                  "estado_civil", "data_nascimento", "cidade_endereco", "escolaridade", "email", "observacao","telefone"]

class BuscaClienteForm(forms.Form):
    nome_cliente = forms.CharField( max_length=45)
    cpf = forms.CharField(max_length=11)
    labels = {
            "nome_cliente": "Nome",
            "cpf": "CPF",
        }
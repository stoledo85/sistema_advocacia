from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Endereco(models.Model):

    UF = (
        ("AC", "Acre"), ("AL", "Alagoas"),
        ("AP", "Amapá"), ("AM", "Amazonas"),
        ("BA", "Bahia"), ("CE", "Ceará"),
        ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
        ("GO", "Goiás"), ("MA", "Maranhão"),
        ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"), ("PA", "Pará"),
        ("PB", "Paraíba"), ("PR", "Paraná"),
        ("PE", "Pernanbuco"), ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"),
        ("RR", "Roraima"), ("SC", "Santa Catarina"),
        ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins"),
    )

    logradouro_endereco = models.CharField(
        verbose_name="Endereço do Cliente", max_length=40)
    nro_endereco = models.IntegerField(
        verbose_name="Número do Cliente", null=True, blank=True)
    nome_bairro = models.CharField(verbose_name="Bairro", max_length=45)
    cidade_endereco = models.CharField(verbose_name="Cidade", max_length=15)
    nome_uf = models.CharField(verbose_name="UF", max_length=2, choices=UF)
    cep = models.CharField(verbose_name="CEP", max_length=8)

    def __str__(self):
        return self.logradouro_endereco


"""Modelo Cliente"""


class Cliente(models.Model):

    ESTADO_CIVIL = (
        ("S", "Solteiro"),
        ("C", "Casado"),
        ("D", "Divorciado"),
        ("U", "União Estavel"),
        ("V", "Viuvo(a)"),
    )

    ESCOLARIDADE = (
        ("FI", "Ensino Fundamental Incompleto"),
        ("FC", "Ensino Fundamental Completo"),
        ("MI", "Ensino Médio Incompleto"),
        ("MC", "Ensino Médio Completo"),
        ("SI", "Ensino Superior Incompleto"),
        ("SC", "Ensino Superior Completo"),
    )
    nome_cliente = models.CharField(
        verbose_name="Nome", max_length=100)
    ctps_cliente = models.CharField(
        verbose_name="Carteira de Trabalho", max_length=10)
    profissao_cliente = models.CharField(
        verbose_name="Profissão", max_length=50)
    cpf = models.CharField(verbose_name="Número do CPF", max_length=14)
    rg = models.CharField(verbose_name="Número de RG", max_length=8)
    nacionalidade = models.CharField(
        verbose_name="Nacionalidade", max_length=50)
    estado_civil = models.CharField(
        verbose_name="Estado Civil", max_length=1, choices=ESTADO_CIVIL)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    cidade_endereco = models.ForeignKey(Endereco, verbose_name="Endereço", on_delete=models.CASCADE)
    escolaridade = models.CharField(
        verbose_name="Escolaridade", max_length=2, choices=ESCOLARIDADE)
    email = models.EmailField(verbose_name="E-mail", max_length=254)
    telefone = models.CharField(verbose_name="Telefone", max_length=11)
    observacao = models.TextField(verbose_name="Obs")

    def __str__(self):
        return self.nome_cliente

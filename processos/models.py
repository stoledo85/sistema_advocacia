from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from clientes.models import Cliente

class Processo(models.Model):
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

    cliente = models.ForeignKey(
        Cliente, verbose_name="Cliente", on_delete=models.PROTECT)
    area_atuacao = models.CharField(
        verbose_name="Area de Atuação", max_length=50)
    obj_acao = models.CharField(verbose_name="Objetivo da Ação", max_length=50)
    cnj = models.CharField(verbose_name="Nro do Processo(CNJ)", max_length=20)
    local_tramite = models.CharField(verbose_name='Tramite', max_length=15)
    tramite_uf = models.CharField(verbose_name="UF", max_length=2, choices=UF)
    nro_processo = models.CharField(verbose_name="Processo", max_length=20)
    # Advogado Responsavel a ser vinculado com o user.
    advogado = models.ForeignKey(
        User, verbose_name="Advogado Responsavel", on_delete=models.DO_NOTHING)
    dt_contratacao = models.DateField(verbose_name="Data da Contratação")
    dt_execucao = models.DateField(verbose_name="Data de Execução")
    dt_sentenca = models.DateField(verbose_name="Data da Sentença")
    vlr_causa = models.DecimalField(
        verbose_name="Valor da Causa", max_digits=5, decimal_places=2)
    pedido = models.CharField(verbose_name="Pedido", max_length=50)
    obs = models.TextField(verbose_name="Obs")

    def __str__(self):
        return self.cliente + " - " + self.nro_processo


class faseProcesso(models.Model):

    tipo_fase_processo = models.CharField(verbose_name='Tipo', max_length=50)
    desc = models.TextField(verbose_name='Descrição')
    processo = models.ForeignKey(
        Processo, verbose_name="Processo", on_delete=models.PROTECT)
    

    def __str__(self):
        return self.tipo_fase_processo + " - " + self.processo

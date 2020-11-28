from django.db import models

# Create your models here.

"""Modelo Cliente"""


class Cliente(models.Model):

    ESTADO_CIVIL = (
        ("S", "Solteiro"),
        ("C", "Casado"),
        ("D", "Divorciado"),
        ("U", "União Estavel"),
        ("V", "Viuvo(a)"),
    )
    
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
    nome_cliente = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=8)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=100)
    nro_endereco = models.IntegerField(null=True, blank=True)
    bairro = models.CharField(max_length=45)
    cidade = models.CharField(max_length=15)
    estado = models.CharField(max_length=2, choices=UF)
    cep = models.CharField(max_length=8)
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome_cliente

from django.db import models

class Cliente(models.Model):
    """Model que compoe a classe Cliente.
    Args:
    nome_cliente(variable) : CharField -- Recebe o Nome completo do Cliente(Campo Obrigatorio).
    cpf(variable) : CharField -- Campo do CPF não formatado com pontos ou infens(Campo Obrigatorio).
    rg(variable) : models.CharField -- Campo do RG não formatado com pontos ou infens(Campo Obrigatorio).
    estado_civil(list) : CharField -- Lista selecionavel do estado civil do cliente.
    data_nascimento(variable) = DateField -- Data de nascimento no formato DD/MM/AAAA(Campo Obrigatorio).
    endereco(variable) = CharField -- Recebe o Logradouro do Cliente.
    nro_endereco(variable) = IntegerField -- Número do Imovel.
    bairro(variable) = CharField -- Campo que recebe o Bairro.
    cidade(variable) = CharField -- Campo que recebe o nome da Cidade.
    estado(list) = CharField -- Lista selecionavel da Unidade federativa ou estado.
    cep(variable) = CharField -- Campo que recebe o CEP sem formatação.
    email(variable) = EmailField -- Campo que recebe o endereço de email com validação de campo.
    telefone(variable) = CharField -- Recebe o numero de telefone no formato (XX)XXXX - XXXX
    """

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

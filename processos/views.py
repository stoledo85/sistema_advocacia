from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProcessoForm, faseProcessoForm, BuscaProcessosForm
from .models import Processo
# Create your views here.

def processoView(request):
    context = {}
    form = ProcessoForm()
    context['form'] = form
    if request.method == "POST":
        resultado = ProcessoForm(request.POST)
        if resultado.is_valid():
            resultado.save()
            sucesso = "Salvo com Sucesso!"
            context['sucesso'] = sucesso
        else:
            erro = "Erro! Cadastro não salvo."
            context['erro'] = erro
    return render(request, "processos/processo.html", context)


def faseProcessoView(request):
    context = {}
    form = faseProcessoForm()
    context['form'] = form
    if request.method == "POST":
        resultado = faseProcessoForm(request.POST)
        if resultado.is_valid():
            resultado.save()
            sucesso = "Salvo com Sucesso!"
            context['sucesso'] = sucesso
        else:
            erro = "Erro! Cadastro não salvo."
            context['erro'] = erro
    return render(request, "processos/faseprocesso.html", context)

def listagemProcessos(request):
    """Gera uma grade com todos os registros dos clientes.
    Busca todos os registros através de um FOR retornando o resultado como objeto.
    """
    processos = []
    # Pesquisar Queryset
    form = BuscaProcessosForm()
    if request.method == "POST":
        resultado = BuscaProcessosForm(request.POST)
        if resultado.is_valid():
            numero = resultado.cleaned_data["cnj"]
            processos = Processo.objects.filter(cnj = numero)
    else:
        processos = Processo.objects.all()

    contexto = {'processos': processos, "form": form}
    return render(request, "processos/listarProcessos.html", contexto)
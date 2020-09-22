from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProcessoForm, faseProcessoForm
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


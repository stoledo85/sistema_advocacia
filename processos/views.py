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
    return render(request, "processos/listarprocessos.html", contexto)


from django.shortcuts import get_object_or_404, redirect
from .models import faseProcesso

def detalheProcesso(request, processo_id):
    processo = get_object_or_404(Processo, id=processo_id)
    fases = faseProcesso.objects.filter(processo=processo)
    context = {
        "processo": processo,
        "fases": fases
    }
    return render(request, "processos/detalhe_processo.html", context)

def excluirProcesso(request, processo_id):
    processo = get_object_or_404(Processo, id=processo_id)
    if request.method == "POST":
        processo.delete()
        return redirect("processos:listaprocessos")
    return render(request, "processos/excluir_processo.html", {"processo": processo})

def atualizarProcesso(request, processo_id):
    processo = get_object_or_404(Processo, id=processo_id)
    if request.method == "POST":
        form = ProcessoForm(request.POST, instance=processo)
        if form.is_valid():
            form.save()
            return redirect("processos:detalhe_processo", processo_id=processo.id)
    else:
        form = ProcessoForm(instance=processo)
    return render(
        request, "processos/atualizar_processo.html", {"form": form, "processo": processo}
    )

def atualizarFase(request, fase_id):
    fase = get_object_or_404(faseProcesso, id=fase_id)
    if request.method == "POST":
        form = faseProcessoForm(request.POST, instance=fase)
        if form.is_valid():
            form.save()
            return redirect("processos:detalhe_processo", processo_id=fase.processo.id)
    else:
        form = faseProcessoForm(instance=fase)
    return render(
        request, "processos/atualizar_fase.html", {"form": form, "fase": fase}
    )

def excluirFase(request, fase_id):
    fase = get_object_or_404(faseProcesso, id=fase_id)
    if request.method == "POST":
        processo_id = fase.processo.id
        fase.delete()
        return redirect("processos:detalhe_processo", processo_id=processo_id)
    return render(request, "processos/excluir_fase.html", {"fase": fase})
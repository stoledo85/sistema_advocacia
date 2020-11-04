from django.http import HttpResponse
from django.http import request
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)

from .forms import BuscaClienteForm, CriarCliente
from .models import Cliente

# Create your views here.


def index(request):
    return render(request, "clientes/index.html")


def clienteView(request):
    context = {}
    form = CriarCliente()
    context['form'] = form
    if request.method == "POST":
        resultado = CriarCliente(request.POST)
        if resultado.is_valid():
            resultado.save()
            sucesso = "Cliente Salvo com Sucesso"
            context["sucesso"] = sucesso
        else:
            erro = "Cliente nao foi salvo"
            context["erro"] = erro
    return render(request, "clientes/cliente.html", context)


def listagemCliente(request):
    clientes = []
    # Pesquisar Queryset
    form = BuscaClienteForm()
    if request.method == "POST":
        resultado = BuscaClienteForm(request.POST)
        if resultado.is_valid():
            nome = resultado.cleaned_data["nome_cliente"]
            cpf = resultado.cleaned_data["cpf"]
            clientes = Cliente.objects.filter(nome_cliente=nome)
        else:
            pass
    else:
        clientes = Cliente.objects.all()

    contexto = {'clientes': clientes, "form": form}
    return render(request, "clientes/listaClientes.html", contexto)


def updateCliente(request, cliente_id):
    cliente_id = int(cliente_id)
    try:
        cliente_sel = Cliente.objects.get(cliente_id = id)
    except Cliente.DoesNotExist:
        return redirect('index')
    CriarCliente = Cliente(request.POST or None, instance = cliente_sel)
    if(CriarCliente.is_valid()):
        CriarCliente.save()
        return redirect('index')
    return render(request, 'cliente/cliente.html',{'CriarCliente':Cliente})

def deleteCliente(request, cliente_id):
    cliente_id = int(cliente_id)
    try:
        cliente_sel = Cliente.objects.get(cliente_id = id)
    except Cliente.DoesNotExist:
        return redirect('index')
    CriarCliente.delete()
    contexto = {'clientes': clientes, "form": form}
    return render(request, "clientes/listaClientes.html", contexto)
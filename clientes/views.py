from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404, HttpResponseRedirect
from .models import Cliente
from .forms import ClienteForm, EnderecoForm, BuscaClienteForm

# Create your views here.


def index(request):
    return render(request, "clientes/index.html")


def enderecoView(request):
    context = {}
    form = EnderecoForm()
    context['form'] = form
    if request.method == "POST":
        resultado = EnderecoForm(request.POST)
        if resultado.is_valid():
            resultado.save()
            sucesso = "Endereço Salvo com Sucesso"
            context["sucesso"] = sucesso
        else:
            erro = "Endereço não foi salvo"
            context["erro"] = erro
    return render(request, "clientes/endereco.html", context)


def clienteView(request):
    context = {}
    form = ClienteForm()
    context['form'] = form
    if request.method == "POST":
        resultado = ClienteForm(request.POST)
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
    #Pesquisar Queryset
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
    
    contexto = {'clientes': clientes, "form":form}
    return render(request, "clientes/listaClientes.html", contexto)

def editarCliente(request, id): 
        pass
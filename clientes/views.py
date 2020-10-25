from django.http import HttpResponse
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)

from .forms import BuscaClienteForm, ClienteForm
from .models import Cliente

# Create your views here.


def index(request):
    return render(request, "clientes/index.html")


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


def updateCliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(instance=cliente)
    if(request.method == 'POST'):
        form = ClienteForm(request.POST, instance=cliente)
        
        if(form.is_valid()):
            cliente = form.save(commit=False)
            Cliente.nome_cliente = form.cleaned_data['nome']
            Cliente.cpf = form.cleaned_data['cpf']
            Cliente.rg = form.cleaned_data['rg']
            Cliente.estado_civil = form.cleaned_data['estado_civil']
            Cliente.data_nascimento = form.cleaned_data['data_nascimento']
            Cliente.endereco = form.cleaned_data['endereco']
            Cliente.nro_endereco = form.cleaned_data['nro_endereco']
            Cliente.bairro = form.cleaned_data['bairro']
            Cliente.cidade = form.cleaned_data['cidade']
            Cliente.estado = form.cleaned_data['estado']
            Cliente.cep = form.cleaned_data['cep']
            Cliente.email = form.cleaned_data['email']
            Cliente.telefone = form.cleaned_data['telefone']
            Cliente.save()
            return redirect('cliente:listacliente')
        else:
            return render(request, 'cliente/listacliente.html', {'form': form, 'cliente' : cliente})
    elif(request.method == 'GET'):
        return render(request, 'cliente/editarCliente.html', {'form': form, 'cliente' : cliente})
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render

from .forms import BuscaClienteForm, ClienteForm
from .models import Cliente

# Create your views here.


def index(request):
    return render(request, "clientes/index.html")


def clienteView(request):
    """Cadastro de Cliente.
    Recebe um objeto cliente no formulario se o resultado for valido,
    o metodo salva no banco de dados e retorna um popup dizendo que a operação foi feita com sucesso.
    """
    context = {}
    form = ClienteForm()
    context["form"] = form
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


def atualizarCliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("listagem_cliente")
    else:
        form = ClienteForm(instance=cliente)
    return render(
        request, "clientes/atualizar_cliente.html", {"form": form, "cliente": cliente}
    )


def excluirCliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == "POST":
        cliente.delete()
        return redirect("listagem_cliente")
    return render(request, "clientes/excluir_cliente.html", {"cliente": cliente})


def listagemCliente(request):
    clientes = []
    form = BuscaClienteForm()
    if request.method == "POST":
        resultado = BuscaClienteForm(request.POST)
        if resultado.is_valid():
            nome = resultado.cleaned_data["nome_cliente"]
            cpf = resultado.cleaned_data["cpf"]
            clientes = Cliente.objects.filter(nome_cliente=nome)
    else:
        clientes = Cliente.objects.all()

    contexto = {"clientes": clientes, "form": form}
    return render(request, "clientes/listaClientes.html", contexto)

from django.urls import path
from . import views


app_name = "clientes"

# Local onde concentra todas rotas do App Cliente.

urlpatterns = [
    path("", views.index, name="index"),
    path("cliente/", views.clienteView, name="cliente"),
    path("listacliente/", views.listagemCliente, name="listacliente"),
    path(
        "atualizar/<int:cliente_id>/", views.atualizarCliente, name="atualizar_cliente"
    ),
    path("excluir/<int:cliente_id>/", views.excluirCliente, name="excluir_cliente"),
]

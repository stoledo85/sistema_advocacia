from django.urls import path
from . import views


app_name = "clientes"

# Local onde concentra todas rotas do App Cliente.

urlpatterns = [
    
    path("", views.index, name="index"),
    path("cliente/", views.clienteView, name="cliente"),
    path('listacliente/', views.listagemCliente, name="listacliente"), 
]

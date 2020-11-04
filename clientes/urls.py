from django.urls import path
from . import views


app_name = "clientes"

urlpatterns = [
    
    path("", views.index, name="index"),
    path("cliente/", views.clienteView, name="cliente"),
    path('listacliente/', views.listagemCliente, name="listacliente"), 
    path('editar/<int:cliente_id>', views.updateCliente),
    path('deletar/<int:cliente_id>', views.deleteCliente),
]

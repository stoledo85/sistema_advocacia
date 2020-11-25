from django.urls import path
from . import views


app_name = "clientes"

urlpatterns = [
    
    path("", views.index, name="index"),
    path("cliente/", views.clienteView, name="cliente"),
    path('listacliente/', views.listagemCliente, name="listacliente"), 
    #path('editarcliente/<int:id>', views.editarCliente,name="editarCliente"),
]

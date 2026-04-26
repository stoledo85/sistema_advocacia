from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('gerenciamento/', views.lista_usuarios, name='listagem_usuarios'),
    path('gerenciamento/novo/', views.criar_usuario, name='criar_usuario'),
    path('gerenciamento/editar/<int:user_id>/', views.editar_usuario, name='editar_usuario'),
    path('gerenciamento/senha/<int:user_id>/', views.trocar_senha, name='trocar_senha'),
    path('meu-perfil/', views.meu_perfil, name='meu_perfil'),
    path('minha-senha/', views.minha_senha, name='minha_senha'),
]

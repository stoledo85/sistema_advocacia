from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .models import Perfil
from .forms import CustomUserCreationForm, UserUpdateForm

def admin_only(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.perfil.role == 'ADMIN':
            return view_func(request, *args, **kwargs)
        return render(request, 'clientes/index.html', {'erro': 'Acesso negado. Apenas administradores podem acessar esta página.'})
    return wrapper

@login_required
@admin_only
def lista_usuarios(request):
    usuarios = User.objects.all().select_related('perfil')
    return render(request, 'usuarios/listagem_usuarios.html', {'usuarios': usuarios})

@login_required
@admin_only
def editar_usuario(request, user_id):
    usuario_edit = get_object_or_404(User, id=user_id)
    roles = Perfil.ROLE_CHOICES
    
    if request.method == 'POST':
        usuario_edit.first_name = request.POST.get('first_name')
        usuario_edit.last_name = request.POST.get('last_name')
        usuario_edit.email = request.POST.get('email')
        usuario_edit.save()
        
        perfil = usuario_edit.perfil
        perfil.role = request.POST.get('role')
        perfil.save()
        
        messages.success(request, f'Usuário {usuario_edit.username} atualizado com sucesso!')
        return redirect('usuarios:listagem_usuarios')
        
    return render(request, 'usuarios/editar_usuario.html', {
        'usuario_edit': usuario_edit,
        'roles': roles
    })

@login_required
@admin_only
def criar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo usuário criado com sucesso!')
            return redirect('usuarios:listagem_usuarios')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'usuarios/criar_usuario.html', {
        'form': form
    })

@login_required
@admin_only
def trocar_senha(request, user_id):
    usuario_edit = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = SetPasswordForm(usuario_edit, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Senha de {usuario_edit.username} alterada com sucesso!')
            return redirect('usuarios:listagem_usuarios')
    else:
        form = SetPasswordForm(usuario_edit)
    
    return render(request, 'usuarios/trocar_senha.html', {
        'form': form,
        'usuario_edit': usuario_edit
    })

@login_required
def meu_perfil(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seu perfil foi atualizado com sucesso!')
            return redirect('usuarios:meu_perfil')
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'usuarios/meu_perfil.html', {
        'form': form
    })

@login_required
def minha_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantém o usuário logado
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('usuarios:meu_perfil')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'usuarios/minha_senha.html', {
        'form': form
    })

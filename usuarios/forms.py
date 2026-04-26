from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label="Primeiro Nome")
    last_name = forms.CharField(max_length=30, required=False, label="Sobrenome")
    email = forms.EmailField(required=True, label="E-mail")
    role = forms.ChoiceField(choices=Perfil.ROLE_CHOICES, label="Cargo no Sistema")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            # The signal will create the profile, we just update it
            user.perfil.role = self.cleaned_data["role"]
            user.perfil.save()
        return user

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, label="Primeiro Nome")
    last_name = forms.CharField(max_length=30, required=True, label="Sobrenome")
    email = forms.EmailField(required=True, label="E-mail")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

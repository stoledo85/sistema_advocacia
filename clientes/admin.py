from django.contrib import admin

from .models import Cliente, Endereco

# Register your models here.
admin.site.register(Endereco)
admin.site.register(Cliente)
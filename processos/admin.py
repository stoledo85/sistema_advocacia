from django.contrib import admin

from .models import Processo, faseProcesso

# Register your models here.

admin.site.register(Processo)
admin.site.register(faseProcesso)

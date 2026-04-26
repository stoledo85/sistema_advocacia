from django.contrib import admin
from .models import Perfil

# Simple registration to see if it avoids the Python 3.14 context bug
admin.site.register(Perfil)

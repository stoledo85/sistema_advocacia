from django.urls import path
from . import views


app_name = "processos"

urlpatterns = [
    path("processo/", views.processoView, name="processo"), 
    path("faseprocesso/", views.faseProcessoView, name="faseprocesso"),
]

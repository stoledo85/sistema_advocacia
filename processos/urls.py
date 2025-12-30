from django.urls import path
from . import views


app_name = "processos"

urlpatterns = [
    path("processo/", views.processoView, name="processo"), 
    path("faseprocesso/", views.faseProcessoView, name="faseprocesso"),
    path("listaprocessos/", views.listagemProcessos, name="listaprocessos"),
    path("detalhe/<int:processo_id>/", views.detalheProcesso, name="detalhe_processo"),
    path("excluir/<int:processo_id>/", views.excluirProcesso, name="excluir_processo"),
    path("atualizar/<int:processo_id>/", views.atualizarProcesso, name="atualizar_processo"),
    path("fase/atualizar/<int:fase_id>/", views.atualizarFase, name="atualizar_fase"),
    path("fase/excluir/<int:fase_id>/", views.excluirFase, name="excluir_fase"),
]

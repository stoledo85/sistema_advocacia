from django import forms
from django.forms import ModelForm

from .models import Processo, faseProcesso


class ProcessoForm(forms.ModelForm):

    class Meta:
        model = Processo

        fields = [
            "cliente", "area_atuacao", "obj_acao", "cnj",
            "local_tramite", "nro_processo", "advogado", "dt_contratacao",
            "dt_encerramento", "dt_trans_julgado", "dt_execucao",  "dt_sentenca",
            "vlr_causa", "pedido", "obs",
        ]


class faseProcessoForm(forms.ModelForm):
    class Meta:
        model = faseProcesso

        fields = ["tipo_fase_processo", "desc", "processo"]

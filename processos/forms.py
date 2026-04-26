from django import forms
from django.forms import ModelForm

from .models import Processo, faseProcesso
from django.contrib.auth.models import User


class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processo
        fields = '__all__'
        labels = {
            "cliente": "Cliente",
            "area_atuacao": "Área de Atuação",
            "obj_acao": "Objetivo da Ação",
            "cnj": "Número do Processo (CNJ)",
            "local_tramite": "Local de Trâmite",
            "tramite_uf": "UF",
            "advogado": "Advogado Responsável",
            "dt_contratacao": "Data de Contratação",
            "dt_execucao": "Data de Execução",
            "dt_sentenca": "Data da Sentença",
            "vlr_causa": "Valor da Causa",
            "pedido": "Resumo do Pedido",
            "obs": "Observações Adicionais",
            "finalizado": "Processo Finalizado?"
        }
        widgets = {
            "cnj": forms.TextInput(attrs={"placeholder": "0000000-00.0000.0.00.0000"}),
            "dt_contratacao": forms.DateInput(attrs={"type": "date"}),
            "dt_execucao": forms.DateInput(attrs={"type": "date"}),
            "dt_sentenca": forms.DateInput(attrs={"type": "date"}),
            "vlr_causa": forms.TextInput(attrs={"placeholder": "R$ 0,00"}),
            "obj_acao": forms.TextInput(attrs={"placeholder": "Ex: Danos Morais"}),
            "pedido": forms.Textarea(attrs={"rows": 3, "placeholder": "Resumo dos pedidos iniciais..."}),
            "obs": forms.Textarea(attrs={"rows": 3, "placeholder": "Notas internas..."}),
        }

    def __init__(self, *args, **kwargs):
        super(ProcessoForm, self).__init__(*args, **kwargs)
        self.fields['advogado'].queryset = User.objects.filter(perfil__role='ADVOGADO')
        for field_name, field in self.fields.items():
            if type(field.widget) not in (forms.CheckboxInput, forms.RadioSelect):
                # Se o widget já tiver classes, adiciona adv-input, senão cria a classe
                current_class = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f'{current_class} adv-input'.strip()


class faseProcessoForm(forms.ModelForm):
    class Meta:
        model = faseProcesso
        fields = '__all__'
        labels = {
            "tipo_fase_processo": "Tipo de Movimentação",
            "processo": "Processo Vinculado",
            "desc": "Descrição da Fase"
        }
        widgets = {
            "desc": forms.Textarea(attrs={"rows": 4, "placeholder": "Descreva o que ocorreu nesta fase..."}),
        }

    def __init__(self, *args, **kwargs):
        super(faseProcessoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if type(field.widget) not in (forms.CheckboxInput, forms.RadioSelect):
                current_class = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f'{current_class} adv-input'.strip()

        
class BuscaProcessosForm(forms.Form):
    nro_processo = forms.CharField(
        max_length=45, 
        label="Número do Processo",
        widget=forms.TextInput(attrs={"placeholder": "Pesquisar por CNJ...", "class": "adv-input"})
    )

from Agenda.models import Contatos
from django import forms
from django.forms import ModelForm


class AgendaForm(ModelForm):
    class Meta:
        model = Contatos
        fields = '__all__'
        labels = {
            'nome': ('Nome Completo'),
            'email': ('E-mail'),
            'telefone': ('Telefone')
        }
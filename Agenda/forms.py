from Agenda.models import Contatos
from django import forms
from django.forms import ModelForm
#from djongo.models import forms


class AgendaForm(ModelForm):
    class Meta:
        model = Contatos
        fields = '__all__'
        labels = {
            'nome': ('Nome Completo'),
            'email': ('E-mail'),
            'telefone': ('Telefone')
        }

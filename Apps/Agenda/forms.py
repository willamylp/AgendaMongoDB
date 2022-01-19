from django.forms import ModelForm

from .models import Contatos


class AgendaForm(ModelForm):
    class Meta:
        model = Contatos
        fields = '__all__'
        labels = {
            'nome': ('Nome Completo'),
            'email': ('E-mail'),
            'telefone': ('Telefone')
        }
        exclude = ['contatosuser']

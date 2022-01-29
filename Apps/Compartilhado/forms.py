from django.forms import ModelForm

from .models import Compartilhados


class CompartilahadoForm(ModelForm):
    class Meta:
        model = Compartilhados
        fields = ['nome', 'email', 'telefone']
        exclude = ['quemcompar']

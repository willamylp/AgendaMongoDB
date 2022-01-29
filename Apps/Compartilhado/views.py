from Apps.Agenda.models import Contatos
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render  # noqa: F401
from django.views.generic.list import ListView

from .models import Compartilhados


@login_required
def CreateShare(request, id):
    compart = get_object_or_404(Contatos, id=id)
    compart.compartilhado = True
    compart.save()
    cmp = Compartilhados.objects.create(nome=compart.nome,
                                        email=compart.email,
                                        telefone=compart.telefone,
                                        quemcompar=compart.contatosuser)
    cmp.save()
    return redirect('/agenda/ListarContatos')


class ListShare(ListView):
    model = Compartilhados

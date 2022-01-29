from Apps.Agenda.models import Contatos
from django.shortcuts import get_object_or_404, redirect, render  # noqa: F401

from .models import Compartilhados


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

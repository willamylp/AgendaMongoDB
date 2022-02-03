from typing import Final

from Apps.Usuario.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .forms import AgendaForm
from .models import Contatos

CONTATO_LIST: Final = "/agenda/ListarContatos"


@login_required
@require_http_methods(["GET", "POST"])
def registrar_contato(request):
    user = request.user
    userDonoContato = User.objects.get(id=user.id)
    form = AgendaForm(request.POST or None)
    if(form.is_valid()):
        form_copy = form.save(commit=False)
        form_copy.contatosuser = userDonoContato
        form_copy.save()
        messages.success(request, 'Contato Registrado com Sucesso!')
        return redirect(CONTATO_LIST)
    return render(request, './formContato.html', {'form': form, 'user': user})


@login_required
@require_http_methods(["GET"])
def listar_contatos(request):
    """Following the logic of the software, we will have to use the
        authentication feature, more precisely to know which user is
        authenticated to display his contacts | using djando's authentication
        system, login() gives us the option to get user data via request.user
    """
    user = request.user
    contatos = Contatos.objects.filter(contatosuser=user.id).values()
    return render(request, './listarContatos.html', {'contatos': contatos})


@login_required
@require_http_methods(["GET", "POST"])
def atualizar_contato(request, id):
    contato = get_object_or_404(Contatos,  pk=id)  # _id=ObjectId(id)
    form = AgendaForm(request.POST, instance=contato)

    if(form.is_valid()):
        form.save()
        return redirect(CONTATO_LIST)
    return render(request, './formContato.html', {'form': form})


@login_required
@require_http_methods(["GET", "POST"])
def deletar_contato(request, id):
    contatoDelete = get_object_or_404(Contatos, pk=id)  # _id=ObjectId(id)
    contatoDelete.delete()
    return redirect(CONTATO_LIST)

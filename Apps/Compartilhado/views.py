from Apps.Agenda.models import Contatos
from django.shortcuts import redirect, render  # noqa: F401

from .forms import CompartilahadoForm


# Create your views here.
# contatosuser foi quem compartilhou
def CreateShare(request, id):
    compartilhado = Contatos.objects.get(id=id)

    form = CompartilahadoForm(request.POST or None, instance=compartilhado)
    if form.is_valid():
        form_comp = form.save(commit=False)
        form_comp.id_compartilhou = compartilhado.id
        form_comp.save()
        return redirect('/agenda/ListarContatos')
    return render(request, 'create_shared.html', {'form': form})

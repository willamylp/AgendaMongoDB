from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Contatos
from Apps.Usuario.models import User
from .forms import AgendaForm
from django.contrib.auth.decorators import login_required                                   

@login_required
def RegistrarContato(request):
    user = request.user
    userDonoContato = User.objects.get(id=user.id)
    form = AgendaForm(request.POST or None)
    if(form.is_valid()):
        Contatos = form.save(commit=False)
        Contatos.contatosuser = userDonoContato
        form.save()
        messages.success(request, 'Contato Registrado com Sucesso!')
        return redirect('/agenda/ListarContatos')
    return render(request, './formContato.html', {'form': form,'user':user})

@login_required
def ListarContatos(request):
    # Following the logic of the software, we will have to use the authentication feature, more precisely to know which user is authenticated to 
    # display his contacts    |  using djando's authentication system, login() gives us the option to get user data via request.user
    user = request.user
    contatos = Contatos.objects.filter(contatosuser = user.id).values()
    return render(request, './listarContatos.html', {'contatos': contatos})

@login_required
def AtualizarContato(request, id):
    contato = get_object_or_404(Contatos,  pk=id)                 #_id=ObjectId(id)
    form = AgendaForm(request.POST, instance=contato)

    if(form.is_valid()):
        form.save()
        return redirect('/agenda/ListarContatos')
    return render(request, './formContato.html', {'form': form})

@login_required
def DeletarContato(request, id):
    contatoDelete = get_object_or_404(Contatos, pk=id)#_id=ObjectId(id)
    contatoDelete.delete()
    return redirect('/agenda/ListarContatos')

from django.shortcuts import get_object_or_404, redirect, render
from urllib import request
from django.contrib import messages
from .models import Contatos
from .forms import AgendaForm
from Agenda import urls
#import json
#import boto3
#from django.core.serializers.json import DjangoJSONEncoder


def RegistrarContato(request):
    form = AgendaForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        messages.success(request, 'Contato Registrado com Sucesso!')
        return redirect('/ListarContatos')
    return render(request, './formContato.html', {'form': form})

def ListarContatos(request):
    contatos = Contatos.objects.all()
    return render(request, './listarContatos.html', {'contatos': contatos})

def AtualizarContato(request, id):
    contato = get_object_or_404(Contatos, pk=id)
    form = AgendaForm(request.POST or None, instance=contato)
    if(form.is_valid()):
        form.save()
        return redirect('/ListarContatos')
    return render(request, './formContato.html', {'form': form})

def DeletarContato(request, id):
    contatoDelete = get_object_or_404(Contatos, pk=id)
    contatoDelete.delete()
    return redirect('/ListarContatos')

from django.shortcuts import get_object_or_404, redirect, render
from urllib import request
from django.contrib import messages
from .models import Contatos
from .forms import AgendaForm
from Agenda import urls
from bson import ObjectId
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
    contatos = Contatos.objects.all().values()
    
    id2 = Contatos.objects.get(_id=ObjectId())
    print('>>>>>>', id2)
    #print('>>>>>>', contatos[0]['_id'])
    return render(request, './listarContatos.html', {'contatos': contatos})


def AtualizarContato(request, id):
    #contato = Contatos.objects.get(_id=ObjectId(id).valueOf())
    contato = get_object_or_404(Contatos, _id=ObjectId(id))
    form = AgendaForm(request.POST, instance=contato)
    if(form.is_valid()):
        form.save()
        return redirect('/ListarContatos')
    return render(request, './formContato.html', {'form': form})

def DeletarContato(request, id):
    #contatoDelete = get_object_or_404(Contatos, _id=ObjectId(id))
    contatoDelete = Contatos.objects.get(_id=ObjectId(id))
    contatoDelete.delete()
    return redirect('/ListarContatos')

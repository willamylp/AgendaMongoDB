from django.urls import path
from Agenda.views import RegistrarContato, ListarContatos, AtualizarContato, DeletarContato

urlpatterns = [
    path('', RegistrarContato, name="RegistrarContato"),
    path(r'ListarContatos/', ListarContatos, name="ListarContato"),
    #path('', Principal, name="Principal"),
    #path('RegistrarContato/', RegistrarContato, name="RegistrarContato"),
    path(r'^AtualizarContato/(?P<id>[0-9]+)/$', AtualizarContato, name="AtualizarContato"),
    path(r'^DeletarContato/(?P<id>[0-9]+)/$', DeletarContato, name="DeletarContato"),
]

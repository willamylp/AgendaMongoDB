from django.urls import path
from Agenda.views import RegistrarContato, ListarContatos, AtualizarContato, DeletarContato

urlpatterns = [
    #path('', Principal, name="Principal"),
    #path('RegistrarContato/', RegistrarContato, name="RegistrarContato"),

    path('', RegistrarContato, name="RegistrarContato"),
    path('ListarContatos/', ListarContatos, name="ListarContato"),
    path('AtualizarContato/<str:id>', AtualizarContato, name="AtualizarContato"),
    path('DeletarContato/<str:id>', DeletarContato, name="DeletarContato"),
]

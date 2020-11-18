from django.urls import path
from Agenda.views import RegistrarContato, ListarContatos, AtualizarContato, DeletarContato

urlpatterns = [
    path('', RegistrarContato, name="RegistrarContato"),
    path('ListarContatos/', ListarContatos, name="ListarContato"),
    #path('', Principal, name="Principal"),
    #path('RegistrarContato/', RegistrarContato, name="RegistrarContato"),
    path('AtualizarContato/<str:id>', AtualizarContato, name="AtualizarContato"),
    #path('AtualizarContato/'r"^(?P<id>[0-9]+)$", AtualizarContato, name="AtualizarContato"),
    path('DeletarContato/<str:id>', DeletarContato, name="DeletarContato"),
]

from django.urls import path

from .views import (atualizar_contato, deletar_contato, listar_contatos,
                    registrar_contato)

urlpatterns = [
    path('RegistrarContato/', registrar_contato, name="RegistrarContato"),
    path('ListarContatos/', listar_contatos, name="ListarContato"),
    path('AtualizarContato/<str:id>', atualizar_contato,
         name="AtualizarContato"),
    path('DeletarContato/<str:id>', deletar_contato, name="DeletarContato"),
]

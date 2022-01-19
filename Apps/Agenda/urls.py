from django.urls import path

from .views import (AtualizarContato, DeletarContato, ListarContatos,
                    RegistrarContato)

urlpatterns = [
    path('RegistrarContato/', RegistrarContato, name="RegistrarContato"),
    path('ListarContatos/', ListarContatos, name="ListarContato"),
    path('AtualizarContato/<str:id>', AtualizarContato, name="AtualizarContato"
         ),
    path('DeletarContato/<str:id>', DeletarContato, name="DeletarContato"),
]

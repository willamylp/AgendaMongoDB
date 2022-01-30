from Apps.Usuario.models import User
from django.db import models


# Create your models here.
class Contatos(models.Model):
    nome = models.CharField(
        max_length=100,
        blank=False
    )
    email = models.EmailField(
        max_length=254,
        blank=False
    )
    telefone = models.CharField(
        max_length=25,
        blank=False
    )
    compartilhado = models.BooleanField(default=False)
    contatosuser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

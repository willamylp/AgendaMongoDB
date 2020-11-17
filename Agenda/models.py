from django.db import models

# Create your models here.
class Contatos(models.Model):
    nome = models.CharField(
        max_length=100,
        blank=False
    )
    email = models.CharField(
        max_length=100,
        blank=False
    )
    telefone = models.CharField(
        max_length=25,
        blank=False
    )

    def __str__(self):
        return self.nome
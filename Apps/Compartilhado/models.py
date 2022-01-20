from django.db import models


# Create your models here.
class Compartilhados(models.Model):
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
    compcategoria = models.ForeignKey(
        "Categoria.Categorias", blank=True, null=True,
        on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome
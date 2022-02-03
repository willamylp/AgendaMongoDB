from django.db import models


# Create your models here.
class Categorias(models.Model):
    tipo = models.CharField(
        max_length=100,
        blank=False
    )
    descricao = models.TextField()

    def __str__(self):
        return self.tipo

from django.db import models

from .usuario import Usuario


class Auxiliar(models.Model):
    numeroIdentificacionUsuario = models.ForeignKey(
        Usuario, unique=True, on_delete=models.CASCADE, null=False)

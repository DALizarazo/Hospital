
from django.db import models

from .usuario import Usuario


class Medico(models.Model):
    numeroUdentificacionUsuario = models.ForeignKey(
        Usuario, unique=True, on_delete=models.CASCADE, null=False)
    especialidad = models.CharField(max_length=200, default="General")
    registro = models.CharField(max_length=256)

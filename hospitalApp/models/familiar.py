from django.db import models
from .paciente import Paciente

from .usuario import Usuario


class Familiar(models.Model):
    numeroIdentificacionUsuario = models.ForeignKey(
        Usuario, unique=True, on_delete=models.CASCADE, null=False)
    idPacientes = models.ForeignKey(
        Paciente, related_name="Paciente", unique=True, on_delete=models.CASCADE, null=False)

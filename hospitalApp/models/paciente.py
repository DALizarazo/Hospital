from django.db import models
from .medico import Medico

from .usuario import Usuario


class Paciente(models.Model):
    numeroIdentificacionUsuario = models.ForeignKey(
        Usuario, unique=True, on_delete=models.CASCADE, null=False)
    fechaNacimiento = models.DateField(blank=True)
    direccion = models.CharField(max_length=250)
    id_medico = models.ForeignKey(Medico, related_name="Medico", unique=True, on_delete=models.CASCADE, null=False)

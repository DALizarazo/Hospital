from distutils.text_file import TextFile
from django.db import models
from .medico import Medico

from .paciente import Paciente


class HistoriaClinica(models.Model):
    fechaActualizacion = models.DateField()
    idPaciente = models.ForeignKey(
        Paciente, unique=True, on_delete=models.CASCADE, null=False)
    idMedico = models.ForeignKey(
        Medico, unique=True, on_delete=models.CASCADE, null=False)
    examenFisico = models.TextField(blank=True)
    diagnostico = models.TextField(blank=True)
    evolucion = models.TextField(blank=True)
    recomendaciones = models.TextField(blank=True)

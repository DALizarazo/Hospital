from django.db import models

from .paciente import Paciente


class SignosVitales (models.Model):
    fecha = models.DateField()
    idPaciente = models.ForeignKey(
        Paciente, unique=True, on_delete=models.CASCADE, null=False)
    oximetria = models.CharField(max_length=250)
    frecuenciaRespiratoria = models.IntegerField()
    frecuenciaCardiaca = models.IntegerField()
    temperatura = models.CharField(max_length=250)
    glucemia = models.IntegerField()
    presionArterial = models.CharField(max_length=250)

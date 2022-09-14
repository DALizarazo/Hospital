from rest_framework import serializers
from hospitalApp.models.historiaClinica import HistoriaClinica


class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = ['fechaActualizacion', 'idPaciente', 'idMedico',
                  'examenFisico', 'diagnostico', 'evolucion', 'recomendaciones']

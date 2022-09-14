from rest_framework import serializers
from hospitalApp.models.signosvitales import SignosVitales


class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignosVitales
        fields = ['fecha', 'idPaciente', 'oximetria', 'frecuenciaRespiratoria',
                  'frecuenciaCardiaca', 'temperatura', 'glucemia', 'presionArterial']

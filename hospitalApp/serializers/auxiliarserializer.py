from rest_framework import serializers

from hospitalApp.models.auxiliar import Auxiliar


class AuxiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auxiliar
        fields = ['numeroIdentificacionUsuario']

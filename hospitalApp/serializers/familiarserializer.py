from rest_framework import serializers
from hospitalApp.models.familiar import Familiar


class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ['numeroIdentificacionUsuario', 'idPacientes']

from rest_framework import serializers

from hospitalApp.models.usuario import Usuario
from hospitalApp.serializers.auxiliarserializer import AuxiliarSerializer


class UsuarioSerializer(serializers.ModelSerializer):

    auxiliar = AuxiliarSerializer

    class Meta:
        model = Usuario
        fields = ['tipoIdentificacion', 'numeroIdentificacion', 'nombre', 'apellidos',
                  'telefono', 'genero', 'correoElectronico', 'username', 'password', 'rol']

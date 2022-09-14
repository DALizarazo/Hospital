from dataclasses import fields
from rest_framework import serializers
from hospitalApp.models.paciente import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['numeroIdentificacionUsuario',
                  'fechaNacimiento', 'direccion', 'id_medico']

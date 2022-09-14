from django.shortcuts import get_object_or_404
from rest_framework import generics, status, views
from rest_framework.response import Response

from hospitalApp.models import Paciente
from hospitalApp.serializers.pacienteserializer import PacienteSerializer


class PacienteCrear(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PacienteDetalle(generics.RetrieveAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    def detalle(request, id, *args, **kwargs):
        paciente = get_object_or_404(Paciente, pk=id)

        return request

from django.shortcuts import get_object_or_404
from rest_framework import status, views, generics
from rest_framework.response import Response

from hospitalApp.models import Medico
from hospitalApp.serializers.medicoserializer import MedicoSerializer


class MedicoCrear(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = MedicoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicoDetalle(generics.RetrieveAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

    def detalle(request, id, *args, **kwargs):
        medico = get_object_or_404(Medico, pk=id)


        return request

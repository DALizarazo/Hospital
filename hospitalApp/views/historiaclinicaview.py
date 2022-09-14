from django.shortcuts import get_object_or_404
from rest_framework import generics, status, views
from rest_framework.response import Response

from hospitalApp.models import HistoriaClinica
from hospitalApp.serializers.historiaclinicaserializer import HistoriaClinicaSerializer


class HistariaClinicaView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = HistoriaClinicaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HistoriaClinicaDetalle(generics.RetrieveAPIView):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaClinicaSerializer

    def detalle(request, id, *args, **kwargs):
        historiaClinica = get_object_or_404(HistoriaClinica, pk=id)

        return request

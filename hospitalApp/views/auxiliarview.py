from django.shortcuts import get_object_or_404
from rest_framework import generics, status, views
from rest_framework.response import Response

from hospitalApp.models import Auxiliar
from hospitalApp.serializers.auxiliarserializer import AuxiliarSerializer


class AuxiliaCrear(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuxiliarSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuxiliarDetalle(generics.RetrieveAPIView):
    queryset = Auxiliar.objects.all()
    serializer_class = AuxiliarSerializer

    def detalle(request, id, *args, **kwargs):
        auxiliar = get_object_or_404(Auxiliar, pk=id)

        return request

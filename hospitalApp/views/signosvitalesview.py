from django.shortcuts import get_object_or_404
from rest_framework import generics, status, views
from rest_framework.response import Response

from hospitalApp.models import SignosVitales
from hospitalApp.serializers.signosvitalesserializer import SignosVitalesSerializer


class SignosVitalesCrear(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = SignosVitalesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignosVitalesDetalle(generics.RetrieveAPIView):
    queryset = SignosVitales.objects.all()
    serializer_class = SignosVitalesSerializer

    def detalle(request, id, *args, **kwargs):
        signosVistales = get_object_or_404(SignosVitales, pk=id)

        return request

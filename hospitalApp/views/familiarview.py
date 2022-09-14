from django.shortcuts import get_object_or_404
from rest_framework import generics, status, views
from rest_framework.response import Response

from hospitalApp.models import Familiar
from hospitalApp.serializers.familiarserializer import FamiliarSerializer


class FamiliarCrear(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = FamiliarSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FamiliarDetalle(generics.RetrieveAPIView):
    queryset = Familiar.objects.all()
    serializer_class = FamiliarSerializer

    def detalle(request, id, *args, **kwargs):
        familiar = get_object_or_404(Familiar, pk=id)

        return request


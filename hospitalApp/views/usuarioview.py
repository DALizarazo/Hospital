from django.shortcuts import get_object_or_404
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from hospitalApp.models import Usuario
from hospitalApp.serializers.usuarioserializer import UsuarioSerializer


class UsuarioCrear(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {
            "username": request.data["username"],
            "password": request.data["password"]
        }

        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)


class UsuarioDetalle(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def detalle(request, id, *args, **kwargs):
        usuario = get_object_or_404(Usuario, pk=id)

        return request

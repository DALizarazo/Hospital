from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    tipoIdentificacion = models.CharField(max_length=255)
    id = models.IntegerField(id, primary_key=True)
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    telefono = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    correoElectronico = models.EmailField()
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField('Password', max_length=256)
    rol = models.CharField('rol', max_length=200)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    objects = UserManager()
    USERNAME_FIELD = 'username'

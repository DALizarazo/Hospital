"""hospitalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from hospitalApp import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('usuario/', views.UsuarioCrear.as_view()),
    path('usuario/<int:pk>', views.UsuarioDetalle.as_view()),
    path('medico/', views.MedicoCrear.as_view()),
    path('medico/<int:pk>', views.MedicoDetalle.as_view()),
    path('paciente/', views.PacienteCrear.as_view()),
    path('paciente/<int:pk>', views.PacienteDetalle.as_view()),
    path('auxiliar/', views.AuxiliaCrear.as_view()),
    path('auxiliar/<int:pk>', views.AuxiliarDetalle.as_view()),
    path('familiar/', views.FamiliarCrear.as_view()),
    path('familiar/<int:pk>', views.FamiliarDetalle.as_view()),
    path('signosvitales/', views.SignosVitalesCrear.as_view()),
    path('signosvitales/<int:pk>', views.SignosVitalesDetalle.as_view()),
    path('historiaclinica/', views.HistariaClinicaView.as_view()),
    path('historiaclinica/<int:pk>', views.HistoriaClinicaDetalle.as_view()),
]

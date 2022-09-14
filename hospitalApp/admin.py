from django.contrib import admin
from .models.auxiliar import Auxiliar
from .models.familiar import Familiar
from .models.historiaClinica import HistoriaClinica
from .models.medico import Medico
from .models.paciente import Paciente
from .models.signosvitales import SignosVitales
from .models.usuario import Usuario

# Register your models here.

admin.site.register(Auxiliar)
admin.site.register(Familiar)
admin.site.register(HistoriaClinica)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(SignosVitales)
admin.site.register(Usuario)

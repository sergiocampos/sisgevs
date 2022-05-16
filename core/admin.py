from django.contrib import admin
from .models import Municipio, UnidadeSaude
from _esporotricose_humana.models import CasoEsporotricose

# Register your models here.

admin.site.register(Municipio)
admin.site.register(CasoEsporotricose)
admin.site.register(UnidadeSaude)
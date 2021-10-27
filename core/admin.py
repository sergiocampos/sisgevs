from django.contrib import admin
from .models import Municipio, CasoEsporotricose, UnidadeSaude

# Register your models here.

admin.site.register(Municipio)
admin.site.register(CasoEsporotricose)
admin.site.register(UnidadeSaude)
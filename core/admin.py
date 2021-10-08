from django.contrib import admin
from .models import Municipio, CodigoIbge, CasoEsporotricose

# Register your models here.

admin.site.register(Municipio)
admin.site.register(CodigoIbge)
admin.site.register(CasoEsporotricose)
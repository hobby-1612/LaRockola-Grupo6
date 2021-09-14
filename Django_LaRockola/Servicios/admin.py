from django.contrib import admin
from Servicios.models import * #Importamod todos los modelos de nuestra app "Servicios"

# Register your models here.
admin.site.register(Usuario)
admin.site.register(GeneroMusical)
admin.site.register(Canciones)

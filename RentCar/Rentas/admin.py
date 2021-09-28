from django.contrib import admin
from Rentas.models import Clientes, Autos, Rentas

# Register your models here.
# Adicionar una grilla a cada uno de los valore particulares
class panelAdminAutos(admin.ModelAdmin):
    list_display = ["placa","tipo","modelo"]
    # Campo de busqueda
    search_fields = ["placa"]
    #Agregar un filtro al panel de administracion
    list_filter = ["modelo"]


admin.site.register(Clientes)
admin.site.register(Autos,panelAdminAutos)
admin.site.register(Rentas)



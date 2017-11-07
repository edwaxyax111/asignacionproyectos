from django.contrib import admin
from asignacion.models import Empleado, EmpleadoAdmin, Proyecto, ProyectoAdmin

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
# Register your models here.

from django.db import models
from django.contrib import admin

class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    profesion = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    correo = models.EmailField(max_length=70)
    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=120)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    encargado = models.CharField(max_length=60)
    empleados = models.ManyToManyField(Empleado, through='Asignacion')
    def __str__(self):
        return self.nombre_proyecto

class Asignacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1

class EmpleadoAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class ProyectoAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)


# Create your models here.

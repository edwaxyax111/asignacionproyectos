from django import forms
from .models import Proyecto, Empleado

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre_proyecto', 'descripcion', 'presupuesto', 'encargado', 'empleados')
    def __init__(self, *args, **kwargs):
        super(ProyectoForm, self).__init__(*args, **kwargs)

        #self.fields["encargado"].widget = forms.widgets.CheckboxSelectMultiple()
        #self.fields["encargado"].help_text = "Seleccione un empleado encargado"
        #self.fields["encargado"].queryset = Empleado.objects.all()

        self.fields["empleados"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["empleados"].help_text = "Ingrese los empleados que participan en el proyecto"
        self.fields["empleados"].queryset = Empleado.objects.all()


class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = ('nombre', 'apellido', 'fecha_nacimiento','profesion','direccion','telefono','correo')

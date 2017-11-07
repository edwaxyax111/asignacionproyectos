from django.shortcuts import render
from django.utils import timezone
from asignacion.models import Proyecto, Asignacion, Empleado
from django.shortcuts import render, get_object_or_404
from .forms import ProyectoForm
from .forms import EmpleadoForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def proyecto_lista(request):
    proyectos = Proyecto.objects.filter()
    return render(request, 'proyectos/proyecto_lista.html', {'proyectos': proyectos})

def proyecto_detalle(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, 'proyectos/proyecto_detalle.html', {'proyecto': proyecto})

@login_required
def proyecto_nuevo(request):
    if request.method == "POST":
        formulario = ProyectoForm(request.POST)
        if formulario.is_valid():
            proyecto = Proyecto.objects.create(nombre_proyecto=formulario.cleaned_data['nombre_proyecto'], descripcion = formulario.cleaned_data['descripcion'], presupuesto = formulario.cleaned_data['presupuesto'], encargado = formulario.cleaned_data['encargado'])
            for empleado_id in request.POST.getlist('empleados'):
                asignacion = Asignacion(empleado_id=empleado_id, proyecto_id = proyecto.id)
                asignacion.save()
                return redirect('proyecto_lista')
    else:
        formulario = ProyectoForm()
        return render(request, 'proyectos/proyecto_editar.html', {'formulario': formulario})

@login_required
def proyecto_editar(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == "POST":
        formulario = ProyectoForm(request.POST, instance=proyecto)
        if formulario.is_valid():
            proyecto = formulario.save(commit=False)
            proyecto.save()
            return redirect('proyecto_detalle', pk=proyecto.pk)
    else:
        formulario = ProyectoForm(instance=proyecto)
    return render(request, 'proyectos/proyecto_editar.html', {'formulario': formulario})

@login_required
def proyecto_remover(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    proyecto.delete()
    return redirect('proyecto_lista')


def empleado_lista(request):
    empleados = Empleado.objects.filter()
    return render(request, 'proyectos/empleado_lista.html', {'empleados':empleados})

def empleado_detalle(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    return render(request, 'proyectos/empleado_detalle.html', {'empleado': empleado})

@login_required
def empleado_nuevo(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.save()
            return redirect('empleado_lista')
    else:
        form = EmpleadoForm()
        return render(request, 'proyectos/empleado_editar.html', {'form': form})

@login_required
def empleado_editar(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == "POST":
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.save()
            return redirect('empleado_detalle', pk=empleado.pk)
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'proyectos/empleado_editar.html', {'form': form})

@login_required
def empleado_remover(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    empleado.delete()
    return redirect('empleado_lista')


#def proyecto_nuevo(request):
#    if request.method == "POST":
#        formulario = ProyectoForm(request.POST)
#        if formulario.is_valid():
#            proyecto = Proyecto.objects.create(nombre_proyecto=formulario.cleaned_data['nombre_proyecto'], descripcion = formulario.cleaned_data['descripcion'], presupuesto = formulario.cleaned_data['presupuesto'], encargado = formulario.cleaned_data['encargado'])
#            for empleado_id in request.POST.getlist('empleados'):
#                asignacion = Asignacion(empleado_id=empleado_id, proyecto_id = proyecto.id)
#                asignacion.save()
#            messages.add_message(request, messages.SUCCESS, 'Proyecto Guardado Exitosamente')
#        else:
#            formulario = ProyectoForm()
#    return render(request, 'proyectos/proyecto_editar.html', {'formulario': formulario})






# Create your views here.

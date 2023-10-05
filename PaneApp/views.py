from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from PaneApp.forms import ProveedorForm, IngredienteForm, PizzaForm
from .models import Proveedor, Ingrediente



def inicio(request):
    return render(request, "PaneApp/inicio.html")

def proveedores(request):
    return render(request, "PaneApp/proveedores.html")

def pizzas(request):
    return render(request, "PaneApp/pizzas.html")

def crear_proveedor(request):
    if request.method == 'POST':
        miForm = ProveedorForm(request.POST)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            miForm.save()
            return redirect('proveedores')  # Redirige a la página de lista de proveedores
    else:
        miForm = ProveedorForm()
    
    # Obtener la lista de proveedores
    proveedores = Proveedor.objects.all()
    
    return render(request, 'PaneApp/proveedores.html', {'miForm': miForm, 'proveedores': proveedores})

def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    
    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedores')
    
    return render(request, 'PaneApp/borrar_proveedor_confirmar.html', {'proveedor': proveedor})

def ingredientes(request):
    if request.method == 'POST':
        ingrediente_form = IngredienteForm(request.POST)
        if ingrediente_form.is_valid():
            ingrediente = ingrediente_form.save(commit=False)
            # Aquí puedes realizar cualquier otra operación antes de guardar si es necesario
            ingrediente.save()
            return redirect('ingredientes')
    else:
        ingrediente_form = IngredienteForm()
    
    ingredientes = Ingrediente.objects.all()
    
    return render(request, 'PaneApp/ingredientes.html', {'ingrediente_form': ingrediente_form, 'ingredientes': ingredientes})

def borrar_ingrediente(request, ingrediente_id):
    ingrediente = get_object_or_404(Ingrediente, pk=ingrediente_id)
    
    if request.method == 'POST':
        ingrediente.delete()
        return redirect('ingredientes')
    
    return render(request, 'PaneApp/borrar_ingrediente_confirmar.html', {'ingrediente': ingrediente})



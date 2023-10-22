from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from PaneApp.forms import ProveedorForm, IngredienteForm, PizzaForm #FALTA IMPORTAR 'UserRegisterForm'
from .models import Proveedor, Ingrediente, Pizza
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def inicio(request):
    proveedores_result = []
    ingredientes_result = []
    pizzas_result = []

    if request.method == 'POST':
        proveedor_query = request.POST.get('proveedor_query', '')
        ingrediente_query = request.POST.get('ingrediente_query', '')
        pizza_query = request.POST.get('pizza_query', '')

        if proveedor_query:
            proveedores_result = Proveedor.objects.filter(nombre__icontains=proveedor_query)
        
        if ingrediente_query:
            ingredientes_result = Ingrediente.objects.filter(nombre__icontains=ingrediente_query)
        
        if pizza_query:
            pizzas_result = Pizza.objects.filter(nombre__icontains=pizza_query)

    return render(request, "PaneApp/busqueda.html", {
        'proveedores_result': proveedores_result,
        'ingredientes_result': ingredientes_result,
        'pizzas_result': pizzas_result
    })

def proveedores(request):
    return render(request, "PaneApp/proveedores.html")

def pizzas(request):
    if request.method == 'POST':
        pizza_form = PizzaForm(request.POST)
        if pizza_form.is_valid():
            pizza = pizza_form.save(commit=False)
            pizza.save()
            return redirect('pizzas')
    else:
        pizza_form = PizzaForm()
    
    pizzas = Pizza.objects.all()
    
    return render(request, 'PaneApp/pizzas.html', {'pizza_form': pizza_form, 'pizzas': pizzas})

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

def borrar_pizza(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    
    if request.method == 'POST':
        pizza.delete()
        return redirect('pizzas')
    
    return render(request, 'PaneApp/borrar_pizza_confirmar.html', {'pizza': pizza})

def login_request(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"PaneApp/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"PaneApp/inicio.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"PaneApp/inicio.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"PaneApp/login.html", {'form':form} )

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"PaneApp/inicio.html" ,  {"mensaje":"Usuario Creado :)"})


      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"PaneApp/registro.html" ,  {"form":form})
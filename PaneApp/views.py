from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    return render(request, "PaneApp/inicio.html")


def proveedores(request):
    return render(request, "PaneApp/proveedores.html")

def pizzas(request):
    return render(request, "PaneApp/pizzas.html")

def ingredientes(request):
    return render(request, "PaneApp/ingredientes.html")
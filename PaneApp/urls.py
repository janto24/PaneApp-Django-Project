from django.urls import path, include
from PaneApp import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('Inicio/',views.inicio, name='inicio'),
    path('Proveedores/', views.crear_proveedor, name='proveedores'),
    path('Pizzas/', views.pizzas, name='pizzas'),
    path('Ingredientes/', views.ingredientes, name='ingredientes'),
    path('borrar_proveedor/<int:proveedor_id>/', views.borrar_proveedor, name='borrar_proveedor'),
    path('borrar_ingrediente/<int:ingrediente_id>/', views.borrar_ingrediente, name='borrar_ingrediente'),

]
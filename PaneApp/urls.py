from django.urls import path, include
from PaneApp import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('Proovedores/', views.proveedores, name='proveedores'),
    path('Pizzas/', views.pizzas, name='pizzas'),
    path('Ingredientes/', views.ingredientes, name='ingredientes'),

   
]
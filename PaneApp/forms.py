from django import forms
from .models import Proveedor, Ingrediente, Pizza, PizzaIngrediente

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono', 'email']

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nombre', 'descripcion', 'proveedor']

    def __init__(self, *args, **kwargs):
        super(IngredienteForm, self).__init__(*args, **kwargs)
        self.fields['proveedor'].empty_label = 'Seleccione un proveedor'


    def __init__(self, *args, **kwargs):
        super(IngredienteForm, self).__init__(*args, **kwargs)
        self.fields['proveedor'].empty_label = 'Seleccione un proveedor'


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['nombre', 'descripcion']


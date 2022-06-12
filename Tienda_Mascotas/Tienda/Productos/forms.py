from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'stock', 'descripcion', 'precio']
        labels = {
            'nombre': 'Nombre',
            'stock': 'Stock',
            'descripcion': 'Descripción',
            'precio': 'Precio'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
        }

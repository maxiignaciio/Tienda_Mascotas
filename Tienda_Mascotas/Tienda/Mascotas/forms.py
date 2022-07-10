from django import forms
from django.forms import fields
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['foto','nombre', 'anios', 'raza', 'descripcion']
        labels = {
            'foto': 'Foto',
            'nombre': 'Nombre',
            'anios': 'Años',
            'raza': 'Raza',
            'descripcion': 'Descripción'
        }
        widgets = {
            'foto':forms.FileInput(attrs={'class':'form-control','type':'file'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'anios': forms.TextInput(attrs={'class': 'form-control'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }

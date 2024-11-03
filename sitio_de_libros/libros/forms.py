from django import forms
from .models import Book

class FormLibro(forms.Form):
    titulo = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Titulo'})
    )
    autor = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Autor'})
    )
    valoracion = forms.IntegerField(
        min_value=0,
        max_value=10000,  # Asegúrate de que este valor esté alineado con tu modelo
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la valoración'})
)


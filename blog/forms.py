from django import forms
from .models import Autor, Categoria, Articulo

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'autor', 'categoria']

class BusquedaForm(forms.Form):
    titulo = forms.CharField(label='Buscar por título', max_length=100)
from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, ArticuloForm, BusquedaForm
from .models import Articulo

def home(request):
    return render(request, 'blog/home.html')

def crear_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/crear_autor.html', {'form': form})

def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/crear_categoria.html', {'form': form})

def crear_articulo(request):
    form = ArticuloForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/crear_articulo.html', {'form': form})

def buscar_articulo(request):
    resultados = []
    if request.GET.get('titulo'):
        form = BusquedaForm(request.GET)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultados = Articulo.objects.filter(titulo__icontains=titulo)
    else:
        form = BusquedaForm()
    return render(request, 'blog/buscar_articulo.html', {'form': form, 'resultados': resultados})
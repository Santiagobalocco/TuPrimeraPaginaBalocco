from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('autor/', views.crear_autor, name='crear_autor'),
    path('categoria/', views.crear_categoria, name='crear_categoria'),
    path('articulo/', views.crear_articulo, name='crear_articulo'),
    path('buscar/', views.buscar_articulo, name='buscar_articulo'),
]

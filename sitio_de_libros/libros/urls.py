from django.urls import path
from . import views
from .models import Book

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para index.html
    path('navbar/', views.navbar, name='navbar'),  # Ruta para navbar.html
    path('libros/', views.mostrar, name='lista_libros'),  # Ruta para lista de libros.html
    path('footer/', views.footer, name='footer'),  # Ruta para lista de libros.html
    path('ingresar_libro/', views.ingresar_libro, name='ingresar_libro'),  # Ruta para ingreso de libros.html
    
    
]


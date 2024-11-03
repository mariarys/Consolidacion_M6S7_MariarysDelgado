from django import forms  # Importa forms
from django.shortcuts import render, redirect
from django.contrib import messages

# Definición de la clase Libro
class Libro(object):
    def __init__(self, titulo, autor, valoracion):
        self.titulo = titulo
        self.autor = autor
        self.valoracion = valoracion

# Lista de libros predefinida (almacenados en memoria)
libros = [
    Libro('Django 3 Web Development Cookbook Fourth Edition', 'Aidas Bendoraitis', 3250),
    Libro('Django for Beginners', 'William S. Vincent', 1800),
    Libro('Two Scoops of Django 3.x', 'Daniel Roy Greenfeld & Audrey Roy Greenfeld', 2200),
    Libro('Test-Driven Development with Python', 'Harry J.W. Percival', 2500),
    Libro('Lightweight Django', 'Julia Elman & Mark Lavin', 1450),
    Libro('Building APIs with Django', 'Hulbert Evan', 1650),
    Libro('Practical Django Projects', 'James Bennett', 1300),
    Libro('Mastering Django', 'Nigel George', 1700),
    Libro('High Performance Django', 'Peter Baumgartner & Yann Malet', 1550),
    Libro('Definitive Guide to Django: Web Development Done Right', 'Adrian Holovaty & Jacob Kaplan-Moss', 1400)
]

def navbar(request):
    return render(request, 'libros/navbar.html')  # Renderiza navbar.html

def index(request):
    return render(request, 'libros/index.html')  # Renderiza index.html

def mostrar(request):
    libros_valoracion_alta = [libro for libro in libros if libro.valoracion > 1500]

    contexto = {
        'libros_valoracion_alta': libros_valoracion_alta,
        'libros': libros
    }

    return render(request, 'libros/lista_libros.html', contexto) 

def footer(request):
    return render(request, 'libros/footer.html')  # Renderiza footer.html

# Formulario para ingresar libros
class FormLibro(forms.Form):
    titulo = forms.CharField(max_length=200)
    autor = forms.CharField(max_length=100)
    valoracion = forms.IntegerField()

def ingresar_libro(request):
    if request.method == 'POST':  
        form = FormLibro(request.POST)  
        if form.is_valid(): 
            # Agregar el nuevo libro a la lista existente
            nuevo_libro = Libro(
                form.cleaned_data['titulo'],
                form.cleaned_data['autor'],
                form.cleaned_data['valoracion']
            )
            libros.append(nuevo_libro)  # Almacena el libro en la lista
            messages.success(request, 'Libro creado correctamente')  
            return redirect('lista_libros')  # Redirige a la lista de libros
        else: 
            messages.error(request, 'Modifica los datos de ingreso')  
            return redirect('ingresar_libro') 
    else:  
        form = FormLibro()  # Crea una instancia vacía del formulario
    return render(request, 'libros/ingresar_libro.html', {'form': form})  # Renderiza la plantilla con el formulario

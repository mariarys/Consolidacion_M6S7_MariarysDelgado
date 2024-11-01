from django.shortcuts import render

def navbar(request):
    return render(request, 'libros/navbar.html')  # Renderiza navbar.html

def index(request):
    return render(request, 'libros/index.html')  # Renderiza index.html

class Libro(object):
    def __init__(self,titulo,autor,valoracion):
        self.titulo = titulo
        self.autor = autor
        self.valoracion = valoracion


def mostrar(request):
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

    libros_valoracion_alta = [libro for libro in libros if libro.valoracion > 1500]

    contexto = {
        'libros_valoracion_alta': libros_valoracion_alta,
        'libros': libros
    }

    return render(request, 'libros/lista_libros.html', contexto) 
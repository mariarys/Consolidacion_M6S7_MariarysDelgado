from django.shortcuts import render

def navbar(request):
    return render(request, 'libros/navbar.html')  # Renderiza navbar.html

def index(request):
    return render(request, 'libros/index.html')  # Renderiza index.html

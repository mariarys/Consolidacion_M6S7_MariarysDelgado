from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para index.html
    path('navbar/', views.navbar, name='navbar'),  # Ruta para navbar.html
]


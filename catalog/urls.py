from django.urls import path

from . import views

urlpatterns = [
    path('buscar_libro/', views.buscar_libro, name='buscar_libro'),
]
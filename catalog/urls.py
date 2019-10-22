from django.urls import path

from . import views, models

urlpatterns = [
    path('buscar_libro/', views.buscar_libro, name='buscar_libro'),
    path('listar_libros/', views.listar, {'modelo': models.Libro}, name='listar_libros'),
    path('listar_autores/', views.listar, {'modelo': models.Autor}, name='listar_autores'),
]
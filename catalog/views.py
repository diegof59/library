from django.shortcuts import render
from django.http import HttpResponse

from .models import Libro

def buscar_libro(request):

    errors = []

    if 'query' in request.GET:
        
        query = request.GET['query']

        if not query:
            errors.append('Introduce un término de búsqueda.')
        elif len(query) >= 25:
            errors.append('Introduce un término de búsqueda menor a 25 caracteres.')
        else:
            libros = Libro.objects.filter(titulo__icontains = query)
            context = {'libros': libros, 'query': query}
            return render(request, 'catalog/libro_query.html', context)
    
    return render(request, 'catalog/buscar_libro.html', {'errors': errors})

def listar(request, **kwargs):

    modelo = kwargs['modelo']
    lista = modelo.objects.all()
    print(lista)
    return render(
                request, 'catalog/listar.html',
                {'lista': lista, 'tipo_objeto': modelo._meta.verbose_name_plural.title()}
            )
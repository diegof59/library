from django.shortcuts import render
from django.http import HttpResponse

from .models import Libro

def buscar_libro(request):
    if 'query' in request.GET:
        query = request.GET['query']
        if query:
            libros = Libro.objects.filter(titulo__icontains = query)
            context = {'libros': libros, 'query': query}
            return render(request, 'catalog/libro_query.html', context)
        else:
            context = {'error': True}
            return render(request, 'catalog/buscar_libro.html', context)
        return HttpResponse(mensaje)
    else:
        return render(request, 'catalog/buscar_libro.html')
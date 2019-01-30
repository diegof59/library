from django.shortcuts import render
from django.http import HttpResponse

def buscar_libro(request):
    if 'query' in request.GET:
        if request.GET['query']:
            mensaje = 'Estas buscando: %r' % request.GET['query']
        else:
            mensaje = 'Haz subido un formulario vacio.'
        return HttpResponse(mensaje)
    else:
        return render(request, 'catalog/buscar_libro.html')
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ContactoForm

# Muestra alguna info incluida en la request.
def show_meta(request):
    
    browser = request.META.get('HTTP_USER_AGENT')
    ref_url = request.META.get('HTTP_REFERER')
    usr_ip = request.META.get('REMOTE_ADDR')
    path = request.path
    response = 'Browser: %s<br> Referer URL: %s<br>Path: %s<br> User IP: %s<br>'%(browser,ref_url,path,usr_ip)
    
    return HttpResponse(response)

# Maneja el formulario de contacto para enviar un mensaje al staff de libreria.
def contactar(request):

    if request.method == 'POST':
        form = ContactoForm(request.POST)

        if form.is_valid():
            datos = form.cleaned_data
            send_mail(
                datos['asunto'],
                datos['mensaje'],
                datos.get('email', 'no-mail@lib.co'),
                ['contacto@lib.co']
            )
            return HttpResponseRedirect('/meta')
    else:
        form = ContactoForm()

    return render(request, 'contactar.html', {'form': form})

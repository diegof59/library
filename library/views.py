from django.http import HttpResponse

def show_meta(request):
    
    browser = request.META.get('HTTP_USER_AGENT')
    ref_url = request.META.get('HTTP_REFERER')
    usr_ip = request.META.get('REMOTE_ADDR')
    response = 'Browser: %s<br> URL: %s<br> User IP: %s<br>'%(browser,ref_url,usr_ip)
    
    return HttpResponse(response)
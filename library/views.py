from django.http import HttpResponse

def show_meta(request):
    
    browser = request.META.get('HTTP_USER_AGENT')
    ref_url = request.META.get('HTTP_REFERER')
    usr_ip = request.META.get('REMOTE_ADDR')
    path = request.path
    response = 'Browser: %s<br> Referer URL: %s<br>Path: %s<br> User IP: %s<br>'%(browser,ref_url,path,usr_ip)
    
    return HttpResponse(response)
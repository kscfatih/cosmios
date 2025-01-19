from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"istek geldi : {request.path}")
        response = self.get_response(request)
        if request.user and request.user.is_authenticated:
            print('user bulundu : ', request.user.username)
        else:
            print('user bulunamadı')
        return response
    
class BlockedIpMiddleware:
    BLOCKED_IPS = ['127.0.0.1']
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
        if ip in self.BLOCKED_IPS:
            return HttpResponseForbidden('Bu ip adresi sistem engellenmiştir')
        
        return self.get_response(request)
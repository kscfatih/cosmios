from django.shortcuts import render, HttpResponse

# Path'ler üzerinden yönlendirdiğimiz kontrol ediciler/viewlar

def index(request):
    # işlem yazıyoruz (database, düz bi cevap)
    return HttpResponse('merhaba dünya')

def blog_ekle(request):
    return HttpResponse('blog eklemeye hoşgeldiniz')
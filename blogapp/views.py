from django.shortcuts import render, HttpResponse
from .models import Blog
# Path'ler üzerinden yönlendirdiğimiz kontrol ediciler/viewlar

def index(request):
    # işlem yazıyoruz (database, düz bi cevap)
    return render(request, 'blogapp/index.html')

def blog_ekle(request):
    return HttpResponse('blog eklemeye hoşgeldiniz')

def blog_detay(request, id):

    context = {
        'id':id,
        'title':'Javascript Öğreniyorum',
        'content':'İçerik'
        }
    return render(request, 'blogapp/blog_detay.html', context)

def blog_liste(request):
    bloglar = [ # veri tabanından gelen format ile aynı
        {'title':'Javascript Öğreniyorum','is_active':1},
        {'title':'Python Öğreniyorum','is_active':0},
        {'title':'Java Öğreniyorum','is_active':1},
        {'title':'Go Öğreniyorum','is_active':1},
        {'title':'C Öğreniyorum','is_active':0},
    ]

    bloglarDemet = [
        ('javascript',1),
        ('C',1),
        ('Go',0),
        ('Java',1)
    ]

    aktif_bloglar = []
    pasif_bloglar = []
    for blog in bloglarDemet:
        if blog[1]:
            aktif_bloglar.append(blog[0])
        else:
            pasif_bloglar.append(blog[0])


    return render(request, 'blogapp/blog_liste.html', {
        'bloglar':bloglar,
        'bloglarDemet':bloglarDemet,
        'pasif':pasif_bloglar,
        'aktif':aktif_bloglar})


def blog_islemleri(request):
    all_blogs = Blog.objects.all()
    active_blogs = Blog.objects.filter(is_active=True) # dönen değer her zaman iterable
    kisisel_gelisim_blogs = Blog.objects.exclude(blog_population='ders')
    try:
        spesifik_blog = Blog.objects.get(id=3) # 1 tane obje döner her durumda böyle. 2 obje olursa hata verir
    except:
        spesifik_blog = None
    
    if Blog.objects.filter(content='C Öğreniyorum içeriği').exists():
        new_blog = Blog.objects.get(content='C Öğreniyorum içeriği')
    else:
        new_blog = Blog.objects.create(
                title='C Öğreniyorum', 
                content='C Öğreniyorum içeriği',
                is_active=True,
                blog_population='ders'
            )
    
    blogInstance, created_status = Blog.objects.get_or_create(
                                        title='C++ Öğreniyorum ',
                                        content='Merhaba dünya ',
                                        defaults={
                                            'is_active':True,
                                            'blog_population':'ders'
                                        })

    context = {'all_blogs':all_blogs,
                'active_blogs':active_blogs,
                'kisisel_gelisim_blogs':kisisel_gelisim_blogs,
                'spesifik_blog':spesifik_blog,
                'new_blog':new_blog,
                'blogInstance':blogInstance,
                'created_status':created_status
            }
    return render(request, 'blogapp/blog_islemleri.html', context)
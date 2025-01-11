from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.views import View
from .forms import *
from django.contrib import messages


# Path'ler üzerinden yönlendirdiğimiz kontrol ediciler/viewlar

def index(request):
    # işlem yazıyoruz (database, düz bi cevap)
    return render(request, 'blogapp/index.html')

def blog_ekle(request):
    return HttpResponse('blog eklemeye hoşgeldiniz')

def blog_detay(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blogapp/blog_detay.html',{'blog':blog})

def blog_liste(request):
    blogs = Blog.objects.filter(is_active = True)
    return render(request, 'blogapp/blog_liste.html', {'blogs':blogs})

def blog_category(request, categoryId):
    category = Category.objects.get(id=categoryId)
    blogs = Blog.objects.filter(category=category)
    return render(request, 'blogapp/blog_liste.html', {'blogs':blogs,'categoryId':categoryId})

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
                                        title='C Öğreniyorum',
                                        content='Merhaba dünya',
                                        defaults={
                                            'is_active':True,
                                            'blog_population':'ders'
                                        })
    
    blogInstance2, created_status2 = Blog.objects.update_or_create(
                                                title='Python Öğreniyorum',
                                                defaults={
                                                    'content':'Python öğreniyorum',
                                                    'is_active':False,
                                                    'blog_population':'kisisel_gelisim'
                                                }
                                            )
    
    tarih_bazli_blog = Blog.objects.order_by('-created')
    title_bazli_blog = Blog.objects.order_by('title')

    toplam_blog = Blog.objects.all().count()
    toplam_ders = Blog.objects.filter(blog_population='ders').count()

    context = {'all_blogs':all_blogs,
                'active_blogs':active_blogs,
                'kisisel_gelisim_blogs':kisisel_gelisim_blogs,
                'spesifik_blog':spesifik_blog,
                'new_blog':new_blog,
                'blogInstance':blogInstance,
                'created_status':created_status,
                'blogInstance2':blogInstance2,
                'created_status2':created_status2,
                'tarih_bazli_blog':tarih_bazli_blog,
                'title_bazli_blog':title_bazli_blog,
                'toplam_blog':toplam_blog,
                'toplam_ders':toplam_ders
            }
    return render(request, 'blogapp/blog_islemleri.html', context)


class KategoriEkle(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'blogapp/kategori_ekle.html',{'form':form})
    
    def post(self, request):
        form = CategoryForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            is_active = form.cleaned_data.get('is_active')
            category, created = Category.objects.get_or_create(name=name, defaults={
                'is_active':is_active
            })
            if created:
                messages.success(request, 'Kategori ekleme başarılı ! '+category.name)
                return redirect('blog_liste')
            else:
                messages.success(request, 'Aynı isimde kategori bulunuyor !')
                return redirect('kategori_ekle')
        else:
            messages.error(request, form.errors)
            return redirect('kategori_ekle')
        

class BlogEkle(View):
    def get(self, request):
        form = BlogForm()
        return render(request, 'blogapp/blog_ekle.html',{'form':form})
    
    def post(self, request):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=True)
            author = Author.objects.get(user=request.user)
            blog.author = author
            blog.save()
            messages.success(request, 'Blog yazınız başarılı şekilde kayıt edildi !')
            return redirect('blog_liste')
        else:
            messages.error(request, form.errors)
            return redirect('blog_ekle')
        
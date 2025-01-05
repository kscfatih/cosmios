from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blog-detay/<int:id>',views.blog_detay, name='blog_detay'),
    path('blog-liste', views.blog_liste, name='blog_liste'),
    path('blog-islemleri', views.blog_islemleri, name='blog_islemleri'),
    path('blog-category/<int:categoryId>', views.blog_category, name='blog_category'),
    path('kategori-ekle',views.KategoriEkle.as_view(), name='kategori_ekle'),
    path('blog-ekle', views.BlogEkle.as_view(), name='blog_ekle')
]
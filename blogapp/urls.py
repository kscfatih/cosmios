from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blog-ekle',views.blog_ekle, name='blog_ekle'),
    path('blog-detay/<int:id>',views.blog_detay, name='blog_detay'),
    path('blog-liste', views.blog_liste, name='blog_liste'),
    path('blog-islemleri', views.blog_islemleri, name='blog_islemleri')
]
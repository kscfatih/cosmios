from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('blog-ekle',views.blog_ekle)
]
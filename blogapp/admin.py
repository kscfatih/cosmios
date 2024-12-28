from django.contrib import admin
from .models import Blog
# Buradan admin panelin içerisine modellerimizi ekliyoruz
admin.site.site_title='Blog Projesi'
admin.site.site_header='Blog Projesi'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_active',
        'blog_population',
        'created',
        'updated'
    ]
    list_filter = [
        'is_active',
        'blog_population',
        'created',
        'updated'
    ]
    search_fields = [
        'title',
        'content',
        'blog_population'
    ]
    fieldsets = [
        (
            'Başlık ve İçerik Bilgileri',
            {
                'fields':['title','content']
            }
        ),
        (
            'Diğer Bilgiler',
            {
                'fields':['is_active','blog_population']
            }
        )
    ]


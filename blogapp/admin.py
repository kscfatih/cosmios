from django.contrib import admin
from .models import Blog, Category, Author
# Buradan admin panelin içerisine modellerimizi ekliyoruz
admin.site.site_title='Blog Projesi'
admin.site.site_header='Blog Projesi'


admin.site.register(Category)
admin.site.register(Author)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'is_active',
        'blog_population',
        'category',
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
                'fields':['is_active','blog_population','category','author']
            }
        )
    ]


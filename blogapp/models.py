from django.db import models
from django.contrib.auth.models import User
BLOG_POPULATION_CHOICES = [
        ('kisisel_gelisim','Kişisel Gelişim'),
        ('ders','Ders')
    ]

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Aktif mi ?", null=True)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author')
    birth_day = models.DateField(null=True, blank=True)
    population = models.CharField(max_length=100, choices=BLOG_POPULATION_CHOICES, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Aktif mi ?", null=True)

    def __str__(self):
        return self.user.first_name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Aktif mi ?", null=True)
    
    def __str__(self):
        return self.name

# Buraya veri tabanı tabloları / modeller oluşturulacak
class Blog(BaseModel):
    title = models.CharField(
        max_length=100, 
        help_text="Max 100 karakter girmelisin", 
        verbose_name='Başlık', null=True)
    content = models.TextField(unique=True, verbose_name="İçerik", null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='blogs')
    blog_population = models.CharField(
        max_length=100, 
        choices=BLOG_POPULATION_CHOICES,
        null=True, # veri tabanına blog_population alanının null olarak kayıt edilmesini sağlar
        blank=True # django formlarında bu alanı boş bırakabilme opsiyonu sunar
    )
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="blogs")
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name="Yazılar"

# Blog & Category
# One to One  models.OneToOneField
# Many To One ForeignKey
# Many To Many 
# xcategory.blogs = x kategorisine ait bloglar verilir (related_name)

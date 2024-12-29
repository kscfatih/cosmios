from django.db import models

BLOG_POPULATION_CHOICES = [
        ('kisisel_gelisim','Kişisel Gelişim'),
        ('ders','Ders')
    ]
# Buraya veri tabanı tabloları / modeller oluşturulacak
class Blog(models.Model):
    title = models.CharField(
        max_length=100, 
        help_text="Max 100 karakter girmelisin", 
        verbose_name='Başlık', null=True)
    content = models.TextField(unique=True, verbose_name="İçerik", null=True)
    is_active = models.BooleanField(default=True, verbose_name="Aktif mi ?", null=True)
    blog_population = models.CharField(
        max_length=100, 
        choices=BLOG_POPULATION_CHOICES,
        null=True, # veri tabanına blog_population alanının null olarak kayıt edilmesini sağlar
        blank=True # django formlarında bu alanı boş bırakabilme opsiyonu sunar
    )
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name="blogs")
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name="Yazılar"

# Blog & Category
# One to One  models.OneToOneField
# Many To One ForeignKey
# Many To Many 
# xcategory.blogs = x kategorisine ait bloglar verilir (related_name)
class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
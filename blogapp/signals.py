from django.db.models.signals import pre_save, post_save
from .models import Blog, Author
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



@receiver(pre_save, sender=Blog)
def before_blog_save(sender, instance, **kwargs):
    print('blog kayıt edilmeden önce')


@receiver(post_save, sender=Blog)
def after_blog_save(sender, instance, created, **kwargs):
    if created:
        print('yeni bir blog oluşturuldu')
    else:
        print('Var olan bir blog objesi güncellendi')


@receiver(post_save, sender=User)
def after_user_save(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)
        print('yeni user yazar olarak eklendi')
    else:
        if Author.objects.filter(user=instance).exists():
            print('bu user bir yazar')
        else:
            Author.objects.create(user=instance)
            print('var olan user yazar olarak eklendi')
from django.db.models.signals import pre_save, post_save
from .models import Blog
from django.dispatch import receiver


@receiver(pre_save, sender=Blog)
def before_blog_save(sender, instance, **kwargs):
    print('yeni title : ',instance.title)
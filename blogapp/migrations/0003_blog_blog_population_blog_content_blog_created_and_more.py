# Generated by Django 5.1.4 on 2024-12-28 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_blog_options_remove_blog_blog_population_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_population',
            field=models.CharField(blank=True, choices=[('kisisel_gelisim', 'Kişisel Gelişim'), ('ders', 'Ders')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.TextField(null=True, unique=True, verbose_name='İçerik'),
        ),
        migrations.AddField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='is_active',
            field=models.BooleanField(default=True, null=True, verbose_name='Aktif mi ?'),
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(help_text='Max 100 karakter girmelisin', max_length=100, null=True, verbose_name='Başlık'),
        ),
        migrations.AddField(
            model_name='blog',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

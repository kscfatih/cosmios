from django.urls import path
from .views import *

urlpatterns = [
    path('categories', category_view, name='api-categories')
]

from django.urls import path
from .views import *

urlpatterns = [
    path('categories', category_view, name='api-categories'),
    path('categories/<int:pk>', category_detail_view, name='api-detail-categories')
]

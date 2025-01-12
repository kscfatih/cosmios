from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blog')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('categories', category_view, name='api-categories'),
    path('categories/<int:pk>', category_detail_view, name='api-detail-categories'),
    path('authors', AuthorsView.as_view(), name='api-authors'),
    path('blogs', BlogListCreate.as_view(), name='api-blogs'),
    path('blogs/<int:pk>', BlogDetailView.as_view(), name='api-detail-blogs'),
    path('router/', include(router.urls))
]

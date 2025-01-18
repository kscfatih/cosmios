from blogapp.models import Category, Blog
from django_filters import rest_framework as filters
import django_filters

class CategoryFilter(filters.FilterSet):
    class Meta:
        model = Category
        fields = ['name','is_active']
# icontains karakter bazlı arama yapar
class BlogFilter(filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')
    is_active = django_filters.BooleanFilter()
    class Meta:
        model = Blog
        fields = ['title','content','category','blog_population']

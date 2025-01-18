from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view
from blogapp.models import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from .pagination import *
import django_filters.rest_framework
from rest_framework import filters


@api_view(['GET','POST'])
def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def category_detail_view(request, pk):
    try:
        category = Category.objects.get(id=pk)
    except:
        return Response('İlgili id ile bir obje bulunamdı',status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)      
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class AuthorsView(APIView):
   
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass

    def post(self, request):
        pass


# ÖDEV !!! yazar için detay view oluşturulacak => Güncelle, Silme ve detay görüntüleme


    


class BlogListCreate(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = BlogPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    

class BlogDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class = BlogSerializer

class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class AuthorViewSet(ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    pagination_class = AuthorPagination


class BlogViewSet(ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogHyperSerializer
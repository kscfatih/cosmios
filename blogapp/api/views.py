from rest_framework.response import Response
from .serializers import CategorySerializer
from rest_framework.decorators import api_view
from blogapp.models import *
from rest_framework import status

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
        return Response('İlgili id ile bir obje bulunamdı',status=status.HTTP_400_BAD_REQUEST)

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
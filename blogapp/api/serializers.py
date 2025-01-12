from rest_framework import serializers
from blogapp.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","first_name","last_name","email"]

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    is_active = serializers.BooleanField(required=False)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    def create(self, valiated_data):
        category = Category.objects.create(**valiated_data)
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        return instance
    


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    is_active = serializers.BooleanField(required=False)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    user = UserSerializer()
    birth_day = serializers.DateField(required=False)
    population = serializers.ChoiceField(choices=BLOG_POPULATION_CHOICES, required=False)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.is_active = validated_data.get('is_active',instance.is_active)
        instance.user = validated_data.get('user',instance.user)
        instance.birth_day = validated_data.get('birth_day',instance.birth_day)
        instance.population = validated_data.get('population', instance.population)
        instance.save()
        return instance


    
class BlogSerializer(serializers.ModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        view_name='category-detail',
        many=True,
        read_only=True
    )
    author = AuthorSerializer()
    class Meta:
        model = Blog
        fields = '__all__'

class BlogHyperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


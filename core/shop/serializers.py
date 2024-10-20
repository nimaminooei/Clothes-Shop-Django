# serializers.py
from rest_framework import serializers
from .models import Category, Products

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']  

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'category', 'image', 'feature', 'price']
        depth = 1 

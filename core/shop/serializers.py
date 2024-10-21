# serializers.py
from rest_framework import serializers
from .models import Category, Products,ProductRating

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']  

class ProductsSerializer(serializers.ModelSerializer):
    user_rate = serializers.SerializerMethodField() 

    class Meta:
        model = Products
        fields = ['id', 'name', 'category', 'image', 'feature', 'price', 'user_rate']
        depth = 1

    def get_user_rate(self, obj):

        request = self.context.get("request", None)
        
        if request and request.user.is_authenticated:
            
            rating = ProductRating.objects.filter(user=request.user, product=obj).first()
            if rating:
                return rating.rating  
        return None 

class ProductRatingSerializer(serializers.ModelSerializer):
    user = serializers.CharField(
        source="user.username", read_only=True)
    class Meta:
        model = ProductRating
        fields = ['product', 'rating', 'review','user'] 

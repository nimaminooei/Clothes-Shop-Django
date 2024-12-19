# serializers.py
from rest_framework import serializers
from .models import Category, Products,ProductRating,Discount

class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'parent', 'children']

    def get_children(self, obj):
        return CategorySerializer(obj.children.all(), many=True).data
    
class DiscountManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'name', 'discount_type', 'value', 'active', 'start_date', 'end_date', 'products']
        
class DiscountSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = Discount
        fields = ['name', 'discount_type', 'value', 'active', 'end_date', 'date']

    def get_date(self, obj):
        if obj.end_date:
            return obj.end_date.strftime('%B %d, %Y') 
        return None
class ProductsSerializer(serializers.ModelSerializer):
    user_rate = serializers.SerializerMethodField() 
    price = serializers.SerializerMethodField()
    original_price = serializers.SerializerMethodField()
    discounts = DiscountSerializer(many=True)
    class Meta:
        model = Products
        fields = ['id', 'name', 'category', 'image', 'feature', 'price', 'user_rate','original_price','discounts']
        depth = 1

    def get_user_rate(self, obj):
        request = self.context.get("request", None)
        if request and request.user.is_authenticated:
            rating = ProductRating.objects.filter(user=request.user, product=obj).first()
            if rating:
                return rating.rating  
        return None 
    
    def get_price(self, obj):
        return obj.get_discounted_price()
    def get_original_price(self, obj):
        return obj.price
class ProductRatingSerializer(serializers.ModelSerializer):
    user = serializers.CharField(
        source="user.username", read_only=True)
    class Meta:
        model = ProductRating
        fields = ['product', 'rating', 'review','user'] 

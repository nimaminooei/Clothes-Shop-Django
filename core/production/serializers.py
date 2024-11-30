# serializers.py

from rest_framework import serializers
from .models import SingleOrder, Order
from shop.models import Products 
from shop.serializers import ProductsSerializer

class SingleOrderSerializer(serializers.ModelSerializer):
    product = ProductsSerializer(source="product.id")
    class Meta:
        model = SingleOrder
        fields = ['id', 'user', 'product', 'count']

class OrderSerializer(serializers.ModelSerializer):
    items = SingleOrderSerializer(many=True)  
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'total_price']
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            SingleOrder.objects.create(order=order, **item_data)
        return order


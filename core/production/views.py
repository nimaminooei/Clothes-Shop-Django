from rest_framework import viewsets,status,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import SingleOrder, Order
from .serializers import SingleOrderSerializer, OrderSerializer
from shop.models import Products

class GetOrder(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user,status=False)
        activeorder = Order.objects.get(user=request.user,status=True)
        return Response({'orderhistory':OrderSerializer(orders,many=True).data,"activeorder":OrderSerializer(activeorder).data},status=status.HTTP_200_OK)


class CartManagerAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        task = request.data.get('task', '').lower()
        product_id = request.data.get('product', None)
        user = request.user
        if not product_id:
            return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        # try:
        #     product = Products.objects.get(id=product_id)
        # except Products.DoesNotExist:
        #     return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        product = get_object_or_404(Products, id=product_id)
        
        if task == 'add':
            return self.add_product_to_order(Order, product, user)
        elif task == 'remove':
            return self.remove_product_from_order(Order, product, user)
        else:
            return Response({"error": "Invalid task"}, status=status.HTTP_400_BAD_REQUEST)
        
    

    def add_product_to_order(self, order, product, user):
        activeorder = Order.objects.filter(user = user , status=True)
        if activeorder.count() > 0:
            single_order, created = SingleOrder.objects.get_or_create(order=activeorder.first(),product=product, user=user)
        else:
            single_order = SingleOrder.objects.create( product=product, user=user)
        if not created:
            single_order.count += 1
        single_order.save()
        return Response(
            {"message": "Product added to order", "single_order": SingleOrderSerializer(single_order).data},
            status=status.HTTP_200_OK
        )
    def remove_product_from_order(self, order, product, user):
        activeorder = Order.objects.filter(user = user , status=True)
        if activeorder.count() == 0:
            return Response({"message": "No active order found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            single_order = SingleOrder.objects.get(order = activeorder.first(), product=product, user=user)
            if single_order.count > 1:
                single_order.count -= 1
                single_order.save()
                return Response(
                    {"message": "Product count decreased", "single_order": SingleOrderSerializer(single_order).data},
                    status=status.HTTP_200_OK
                )
            else:
                single_order.delete()
                return Response({"message": "Product removed from order"}, status=status.HTTP_200_OK)
        except SingleOrder.DoesNotExist:
            return Response({"error": "Product not found in the order"}, status=status.HTTP_404_NOT_FOUND)


class SingleOrderViewSet(viewsets.ModelViewSet):
    queryset = SingleOrder.objects.all()
    serializer_class = SingleOrderSerializer

    def perform_create(self, serializer):
        serializer.save()


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        order.items.clear()  
        serializer = self.get_serializer(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)



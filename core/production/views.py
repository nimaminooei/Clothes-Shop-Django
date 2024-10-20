from rest_framework import viewsets
from rest_framework.response import Response
from .models import SingleOrder, Order
from .serializers import SingleOrderSerializer, OrderSerializer

# Viewset برای SingleOrder
class SingleOrderViewSet(viewsets.ModelViewSet):
    queryset = SingleOrder.objects.all()
    serializer_class = SingleOrderSerializer

    def perform_create(self, serializer):
        serializer.save()

# Viewset برای Order
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
        order.items.clear()  # حذف سفارشات قبلی
        serializer = self.get_serializer(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

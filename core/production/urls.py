# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SingleOrderViewSet, OrderViewSet,CartManagerAPIView,GetOrder
app_name = "production"
router = DefaultRouter()
router.register(r'single-orders', SingleOrderViewSet)  
router.register(r'orders', OrderViewSet)              

urlpatterns = [
    path('api/order/',GetOrder.as_view(),name='product'),
    path('api/product/',CartManagerAPIView.as_view(),name='product'),
    path('api/', include(router.urls)),
]

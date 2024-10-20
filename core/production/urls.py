# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SingleOrderViewSet, OrderViewSet,CartManagerAPIView
app_name = "production"
router = DefaultRouter()
router.register(r'single-orders', SingleOrderViewSet)  # مدیریت سفارش‌های تکی
router.register(r'orders', OrderViewSet)               # مدیریت سفارش کلی

urlpatterns = [
    path('api/product/',CartManagerAPIView.as_view(),name='product'),
    path('api/', include(router.urls)),
]

# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductsViewSet
app_name = "shop"
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)  
router.register(r'products', ProductsViewSet)    

urlpatterns = [
    path('api/', include(router.urls)),  
]

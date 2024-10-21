# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductsViewSet,ProductRatingView,WhishlistView
app_name = "shop"
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)  
router.register(r'products', ProductsViewSet)    

urlpatterns = [
    path('api/wishlist/', WhishlistView.as_view(), name='wishlist'),  
    path('api/rate-product/', ProductRatingView.as_view(), name='rate-product'),  
    path('api/ratings/<int:product_id>/', ProductRatingView.as_view(), name='product-ratings'), 
    path('api/', include(router.urls)),  
    
]

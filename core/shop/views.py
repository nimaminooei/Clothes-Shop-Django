# views.py
from rest_framework import viewsets
from .models import Category, Products,ProductRating,Whishlist
from .serializers import CategorySerializer, ProductsSerializer
from rest_framework import viewsets,status,permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProductRatingSerializer,DiscountManageSerializer
from .models import Discount

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountManageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()  
    serializer_class = CategorySerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all() 
    serializer_class = ProductsSerializer

class ProductRatingView(APIView):
    permission_classes = [permissions.IsAuthenticated] 

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        rating_value = request.data.get('rating')
        review_text = request.data.get('review', '')
        user = request.user

        try:
            product = Products.objects.get(id=product_id)
        except Products.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


        rating, created = ProductRating.objects.update_or_create(
            user=user,
            product=product,
            defaults={'rating': rating_value, 'review': review_text}
        )

        if created:
            return Response({"message": "Rating added successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Rating updated successfully"}, status=status.HTTP_200_OK)

    def get(self, request, product_id, *args, **kwargs):
        try:
            product = Products.objects.get(id=product_id)
        except Products.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        ratings = ProductRating.objects.filter(product=product)
        serializer = ProductRatingSerializer(ratings, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class WhishlistView(APIView):
    permission_classes = [permissions.IsAuthenticated] 

    def post(self, request, *args, **kwargs):
        user = request.user.profile  
        product_id = request.data.get('product')

        try:
            product = Products.objects.get(id=product_id)
        except Products.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


        wishlist, created = Whishlist.objects.get_or_create(user=user, product=product)

        if created:
            return Response({"message": "Product added to wishlist"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Product is already in the wishlist"}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        user = request.user.profile
        product_id = request.data.get('product')

        try:
            product = Products.objects.get(id=product_id)
        except Products.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

      
        try:
            wishlist_item = Whishlist.objects.get(user=user, product=product)
            wishlist_item.delete()
            return Response({"message": "Product removed from wishlist"}, status=status.HTTP_200_OK)
        except Whishlist.DoesNotExist:
            return Response({"error": "Product not found in wishlist"}, status=status.HTTP_400_BAD_REQUEST)
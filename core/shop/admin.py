from django.contrib import admin
from .models import Category, Products,ProductRating,Whishlist

class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'review']
    search_fields = ['user__username', 'product__name'] 
    list_filter = ['rating'] 
    ordering = ['product', 'rating']  



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image') 
    search_fields = ('name',)  

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image')  
    list_filter = ('category',)  
    search_fields = ('name','category') 

class WhishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product'] 
    search_fields = ['user__username', 'product__name']  
    list_filter = ['user'] 
    ordering = ['user', 'product'] 
admin.site.register(Category, CategoryAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductRating, ProductRatingAdmin)
admin.site.register(Whishlist, WhishlistAdmin)
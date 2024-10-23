from django.contrib import admin
from .models import Category, Products,ProductRating,Whishlist,Discount

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

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount_type', 'value', 'active', 'start_date', 'end_date') 
    list_filter = ('discount_type', 'active')  
    search_fields = ('name',) 
    filter_horizontal = ('products',)  


admin.site.register(Discount, DiscountAdmin)  # ثبت مدل تخفیف در پنل مدیریت

admin.site.register(Category, CategoryAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductRating, ProductRatingAdmin)
admin.site.register(Whishlist, WhishlistAdmin)
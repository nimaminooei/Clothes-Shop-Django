from django.contrib import admin
from .models import Category, Products


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image') 
    search_fields = ('name',)  

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image')  
    list_filter = ('category',)  
    search_fields = ('name','category') 


admin.site.register(Category, CategoryAdmin)
admin.site.register(Products, ProductsAdmin)

# admin.py

from django.contrib import admin
from .models import SingleOrder, Order




@admin.register(SingleOrder)
class SingleOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'count', 'order')
    list_filter = ('user', 'product')
    search_fields = ['user__username', 'product__name','order__serial']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price')
    list_filter = ('user',)
    search_fields = ['user__username']


    def total_price(self, obj):
        return obj.total_price()

    total_price.short_description = 'Total Price'

# admin.py

from django.contrib import admin
from .models import SingleOrder, Order

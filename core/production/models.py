from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Products
User = get_user_model()

class SingleOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products,null=True, on_delete=models.SET_NULL)
    count = models.IntegerField(null=False, default=1)
    order = models.ForeignKey('Order',null=True,blank=True ,related_name='items', on_delete=models.SET_NULL)
    
    class Meta:
        unique_together = ('order', 'product') 
    def __str__(self):
        return f"{self.count} x {self.product.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=1)
    serial = models.IntegerField(unique=True)
    def total_price(self):
        return sum([item.product.price * item.count for item in self.items.all()])
    
    def __str__(self):
        return str(self.serial)


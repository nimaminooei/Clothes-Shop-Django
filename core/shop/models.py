from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Profile
from django.utils import timezone
User = get_user_model()
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children'
    )  
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        
        return f"{self.parent.name} -> {self.name}" if self.parent else self.name

    class Meta:
        verbose_name_plural = "Categories"
class Products(models.Model):
    name = models.CharField(max_length=255,null=False, blank=False , unique=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL , null=True) 
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    feature = models.TextField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    stock = models.IntegerField()
    def get_discounted_price(self):
        
        discounts = self.discounts.filter(active=True) 
        price = self.price
        for discount in discounts:
            price = discount.apply_discount(price)
        return price

    def __str__(self):
        return str(self.name)
    
class ProductRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField() 
    review = models.TextField(null=True, blank=True) 

    class Meta:
        unique_together = ('user', 'product') 
    def __str__(self):
        return f"{self.user.username} - {self.product.name}: {self.rating}"
    
class Whishlist(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'product')
    def __str__(self):
        return f"{self.user} - {self.product}"
    
class Discount(models.Model):
    DISCOUNT_TYPES = (
        ('percentage', 'Percentage'),
        ('fixed', 'Fixed Amount'),
    )

    name = models.CharField(max_length=255)
    discount_type = models.CharField(max_length=20, choices=DISCOUNT_TYPES)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    products = models.ManyToManyField('Products', related_name='discounts', blank=True)

    def is_valid(self):
        if not self.active:
            return False
        if self.start_date and self.start_date > timezone.now():
            return False
        if self.end_date and self.end_date < timezone.now():
            return False
        return True

    def apply_discount(self, price):
        if not self.is_valid():
            return price
        if self.discount_type == 'percentage':
            return price * (1 - self.value / 100)
        elif self.discount_type == 'fixed':
            return max(price - self.value, 0)
        return price

    def __str__(self):
        return f'{self.name} - {self.value} ({self.discount_type})'
    


from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True,blank=True)
    def __str__(self):
        return str(self.name)
class Products(models.Model):
    name = models.CharField(max_length=255,null=False, blank=False , unique=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL , null=True) 
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    feature = models.TextField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    stock = models.IntegerField()
    def __str__(self):
        return str(self.name)
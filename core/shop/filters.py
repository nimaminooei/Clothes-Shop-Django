from rest_framework import filters
import django_filters
from .models import Products
class ProductsFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = django_filters.CharFilter(field_name='category', lookup_expr='icontains')

    class Meta:
        model = Products
        fields = ['name', 'price', 'category']

from rest_framework import serializers
from .models import Profile
from django.conf import settings
from shop.serializers import ProductsSerializer
from shop.models import Whishlist

user = settings.AUTH_USER_MODEL


class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Profile
        fields = ['name', 'bio', 'location', 'birth_date', 'profile_picture']

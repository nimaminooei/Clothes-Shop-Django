from rest_framework import serializers
from .models import Profile
from django.conf import settings
user = settings.AUTH_USER_MODEL
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user 
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'location', 'birth_date', 'profile_picture']

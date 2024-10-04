from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated

class ProfileDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user.profile

# class ProfileDetailAPIView(generics.RetrieveUpdateAPIView):
#     # queryset = Profile.objects.filter(user=.request.user)
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         # برگرداندن پروفایل کاربر جاری
#         return self.request.user.profile
#     def get_queryset(self):
#         return Profile.objects.filter(user=self.request.user)  # یا هر شرایط دیگری که می‌خواهید

# class ProfileDetailAPIView(generics.RetrieveAPIView):
#     serializer_class = ProfileSerializer

#     def get_queryset(self):
#         return Profile.objects.filter(user=self.request.user)  # یا هر شرایط دیگری که می‌خواهید

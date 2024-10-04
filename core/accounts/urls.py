from . import views
from django.urls import path, include
from .views import ProfileDetailAPIView
app_name = "accounts"

# from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('profile/', ProfileDetailAPIView.as_view(), name='profile-detail'),
    # # djoser Token & JWT
    path("auth/", include("djoser.urls.authtoken")),
    path("auth/", include("djoser.urls.jwt")),
]

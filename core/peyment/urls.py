from django.urls import path
from .views import PaymentRequestView, PaymentVerifyView

urlpatterns = [
    path('request/', PaymentRequestView.as_view(), name='payment-request'),
    path('verify/', PaymentVerifyView.as_view(), name='payment-verify'),
]

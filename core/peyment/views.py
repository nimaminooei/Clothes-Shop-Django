import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import Payment
from .serializers import PaymentSerializer
from production.models import Order
from rest_framework.permissions import IsAuthenticated
class PaymentRequestView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        order_id = request.data.get('order_id')

        try:
            order = Order.objects.get(id=order_id, user=user, status=True)
        except Order.DoesNotExist:
            return Response({"error": "سفارش پیدا نشد یا متعلق به شما نیست"}, status=status.HTTP_404_NOT_FOUND)


        if hasattr(order, 'payment') and order.payment.status == 'INIT':
            # return Response({"error": "پرداخت در حال انتظار است"}, 
            # status=status.HTTP_400_BAD_REQUEST)
            return Response({
                    "payment_url": f"https://sandbox.zarinpal.com/pg/StartPay/{order.payment.authority}",
                }, status=status.HTTP_200_OK)


        payment = Payment.objects.create(order=order)


        zarinpal_request_url = "https://sandbox.zarinpal.com/pg/v4/payment/request.json"
        # data = {
        #     "MerchantID": settings.ZARINPAL_MERCHANT_ID,
        #     "Amount": order.total_price(), 
        #     "Description": f"پرداخت سفارش {order.serial}",
        #     "CallbackURL": settings.ZARINPAL_CALLBACK_URL,
        # }
        data = {
            "merchant_id": settings.ZARINPAL_MERCHANT_ID,  
            "amount": order.total_price(),  
            "description": f"پرداخت سفارش {order.serial}",
            "callback_url": settings.ZARINPAL_CALLBACK_URL,
            "metadata": {
                "mobile": "09123456789",  
                "order_id": "123456"
            }
        }

        try:
            response = requests.post(zarinpal_request_url, json=data)
            response_data = response.json()
            print(response_data)
            if response_data['data']['code'] == 100:

                payment.authority = response_data['data']['authority']
                payment.save()
                return Response({
                    "payment_url": f"https://sandbox.zarinpal.com/pg/StartPay/{response_data['data']['authority']}",
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "خطا در ایجاد درخواست پرداخت"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class PaymentVerifyView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        authority = request.query_params.get('Authority')
        statuss = request.query_params.get('Status')

        try:

            payment = Payment.objects.get(authority=authority)
            order = payment.order

            if statuss != "OK":
                payment.status = "FAIL"
                payment.save()
                return Response({"message": "پرداخت ناموفق بود"}, status=status.HTTP_400_BAD_REQUEST)


            zarinpal_verify_url = "https://sandbox.zarinpal.com/pg/v4/payment/verify.json"
            data = {
                "merchant_id": settings.ZARINPAL_MERCHANT_ID,
                "amount": int(order.total_price()),
                "authority": authority,
            }
            response = requests.post(zarinpal_verify_url, json=data)
            response_data = response.json()
            if response_data['data']['code'] == 100:
                payment.status = "SUCCESS"
                payment.ref_id = response_data["data"]['ref_id']
                payment.save()  
                order.status = 0 
                order.save()
                return Response({
                    "message": "پرداخت با موفقیت انجام شد",
                    "ref_id": payment.ref_id,
                }, status=status.HTTP_200_OK)
            else:
                payment.status = "FAIL"
                payment.save()
                return Response({"message": "پرداخت ناموفق بود"}, status=status.HTTP_400_BAD_REQUEST)
        except Payment.DoesNotExist:
            return Response({"error": "تراکنش پیدا نشد"}, status=status.HTTP_404_NOT_FOUND)

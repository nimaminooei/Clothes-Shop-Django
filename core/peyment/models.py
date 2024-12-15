from django.db import models
from production.models import Order
class Payment(models.Model):
    TRANSACTION_STATUS = (
        ('INIT', 'Initialized'),
        ('SUCCESS', 'Successful'),
        ('FAIL', 'Failed'),
    )

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment', verbose_name="سفارش")
    authority = models.CharField(max_length=255, null=True, blank=True, verbose_name="Authority")
    ref_id = models.CharField(max_length=255, null=True, blank=True, verbose_name="Ref ID")
    status = models.CharField(max_length=10, choices=TRANSACTION_STATUS, default='INIT', verbose_name="وضعیت تراکنش")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return f"Payment for Order {self.order.serial} - {self.status}"

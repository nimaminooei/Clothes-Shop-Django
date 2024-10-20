# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SingleOrder, Order
from .helpers import generate_order_serial
@receiver(post_save, sender=SingleOrder)
def create_or_add_to_order(sender, instance, created, **kwargs):

    if created:

        order = Order.objects.filter(user=instance.user, status=True).first()


        if not order:
            order = Order.objects.create(user=instance.user, status=True, serial=generate_order_serial())


        instance.order = order
        instance.save()

# Generated by Django 5.1.2 on 2024-10-20 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0003_remove_singleorder_orderid_order_serial_order_status_and_more'),
        ('shop', '0004_alter_products_description_alter_products_feature_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleorder',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='production.order'),
        ),
        migrations.AlterField(
            model_name='singleorder',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.products'),
        ),
    ]

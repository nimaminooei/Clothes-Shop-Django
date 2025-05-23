# Generated by Django 5.1.4 on 2024-12-12 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('production', '0009_delete_productrating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authority', models.CharField(blank=True, max_length=255, null=True, verbose_name='Authority')),
                ('ref_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ref ID')),
                ('status', models.CharField(choices=[('INIT', 'Initialized'), ('SUCCESS', 'Successful'), ('FAIL', 'Failed')], default='INIT', max_length=10, verbose_name='وضعیت تراکنش')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='production.order', verbose_name='سفارش')),
            ],
        ),
    ]

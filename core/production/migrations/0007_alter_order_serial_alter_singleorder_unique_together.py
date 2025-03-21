# Generated by Django 5.1.2 on 2024-10-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0006_alter_singleorder_order'),
        ('shop', '0004_alter_products_description_alter_products_feature_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='serial',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='singleorder',
            unique_together={('order', 'product')},
        ),
    ]

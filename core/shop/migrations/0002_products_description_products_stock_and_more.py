# Generated by Django 5.1.2 on 2024-10-20 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='products',
            name='stock',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

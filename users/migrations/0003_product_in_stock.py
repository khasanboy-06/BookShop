# Generated by Django 5.0.6 on 2024-06-18 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_category_client_product_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
    ]

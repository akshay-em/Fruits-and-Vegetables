# Generated by Django 5.0.4 on 2024-06-04 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_order_details_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_details',
            name='approve',
        ),
    ]
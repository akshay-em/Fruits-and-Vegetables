# Generated by Django 5.0.4 on 2024-06-02 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_order_details_quantity_order_details_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_details',
            name='product_name',
            field=models.CharField(default=0, max_length=255),
        ),
    ]

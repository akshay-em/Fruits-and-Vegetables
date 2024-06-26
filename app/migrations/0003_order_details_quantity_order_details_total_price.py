# Generated by Django 5.0.4 on 2024-06-02 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_order_details_product_id_alter_order_details_approve'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_details',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order_details',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]

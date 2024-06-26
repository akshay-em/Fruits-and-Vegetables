# Generated by Django 5.0.4 on 2024-06-01 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_details',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.product'),
        ),
        migrations.AlterField(
            model_name='order_details',
            name='approve',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

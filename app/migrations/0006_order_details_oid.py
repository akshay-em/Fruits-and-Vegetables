# Generated by Django 5.0.4 on 2024-06-09 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_order_details_approve'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_details',
            name='oid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.customer'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-25 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_order_address_order_apartment_order_building_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='apartment',
            field=models.CharField(max_length=100, verbose_name='квартира'),
        ),
    ]

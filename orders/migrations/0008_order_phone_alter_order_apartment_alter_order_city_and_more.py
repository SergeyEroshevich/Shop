# Generated by Django 4.0.5 on 2022-07-25 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_order_apartment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AlterField(
            model_name='order',
            name='apartment',
            field=models.CharField(blank=True, max_length=100, verbose_name='квартира'),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100, verbose_name='город'),
        ),
        migrations.AlterField(
            model_name='order',
            name='house',
            field=models.CharField(max_length=100, verbose_name='дом'),
        ),
        migrations.AlterField(
            model_name='order',
            name='street',
            field=models.CharField(max_length=100, verbose_name='улица'),
        ),
    ]

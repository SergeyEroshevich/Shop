# Generated by Django 4.0.5 on 2022-07-25 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_adress_profile_apartment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=13),
        ),
    ]
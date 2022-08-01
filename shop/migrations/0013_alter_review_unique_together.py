# Generated by Django 4.0.5 on 2022-07-29 11:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0012_rename_reviews_review'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('user', 'product')},
        ),
    ]

# Generated by Django 2.0.5 on 2018-06-01 10:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CarApp', '0012_remove_carbooked_booked_or_not'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carbooked',
            name='username',
        ),
        migrations.AddField(
            model_name='carbooked',
            name='username',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]

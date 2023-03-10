# Generated by Django 4.1.5 on 2023-01-29 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0009_rename_carr_order_phone_order_start_rent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='car',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cars.car'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

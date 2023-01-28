# Generated by Django 4.1.5 on 2023-01-28 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_order_carr_alter_car_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('street_address', models.CharField(max_length=64)),
                ('post_code', models.CharField(max_length=10)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='departments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.department'),
        ),
    ]
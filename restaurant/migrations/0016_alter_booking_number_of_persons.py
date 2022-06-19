# Generated by Django 3.2.13 on 2022-06-19 12:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0015_booking_number_of_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='number_of_persons',
            field=models.IntegerField(default=2, validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(1)]),
        ),
    ]
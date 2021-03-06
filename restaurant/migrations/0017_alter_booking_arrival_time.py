# Generated by Django 3.2.13 on 2022-06-21 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0016_alter_booking_number_of_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='arrival_time',
            field=models.TimeField(choices=[(datetime.time(17, 0), '17:00'), (datetime.time(17, 3), '17:30'), (datetime.time(18, 0), '18:00'), (datetime.time(18, 3), '18:30'), (datetime.time(19, 0), '19:00'), (datetime.time(19, 3), '19:30'), (datetime.time(20, 0), '20:00'), (datetime.time(20, 3), '20:30'), (datetime.time(21, 0), '21:00')]),
        ),
    ]

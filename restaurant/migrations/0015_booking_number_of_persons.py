# Generated by Django 3.2.13 on 2022-06-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0014_auto_20220618_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='number_of_persons',
            field=models.IntegerField(default=2),
        ),
    ]
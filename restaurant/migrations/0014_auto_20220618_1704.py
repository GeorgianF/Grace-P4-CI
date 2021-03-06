# Generated by Django 3.2.13 on 2022-06-18 17:04

from django.db import migrations, models
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_alter_booking_allergies'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_details',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='allergies',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('No Allergies', 'No Allergies'), ('Dairy', 'Dairy'), ('Eggs', 'Eggs'), ('Fish', 'Fish'), ('Shelfish', 'Shellfish'), ('Nuts', 'Nuts'), ('Peanuts', 'Peanuts'), ('Gluten', 'Gluten'), ('Soy', 'Soy')], max_length=61),
        ),
    ]

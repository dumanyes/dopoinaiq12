# Generated by Django 4.2.6 on 2023-10-29 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turfs', '0009_turfimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='end_time',
            field=models.CharField(default='08:00:00', max_length=8),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='start_time',
            field=models.CharField(default='07:00:00', max_length=8),
        ),
    ]
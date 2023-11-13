# Generated by Django 4.2.6 on 2023-10-28 13:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('turfs', '0003_remove_turf_time_slots_timeslot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslot',
            name='slot',
        ),
        migrations.AddField(
            model_name='timeslot',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-31 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turfs', '0011_timeslot_booked_alter_timeslot_end_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turf',
            name='facilities',
        ),
        migrations.RemoveField(
            model_name='turf',
            name='sports',
        ),
        migrations.AlterField(
            model_name='turf',
            name='info',
            field=models.TextField(default=''),
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sports', models.CharField(max_length=100)),
                ('turf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turfs.turf')),
            ],
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facilities', models.CharField(default='', max_length=100)),
                ('turf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turfs.turf')),
            ],
        ),
    ]

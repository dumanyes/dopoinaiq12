# Generated by Django 4.2.6 on 2023-11-01 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turfs', '0014_turf_owner_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='turf_owner_email',
            field=models.EmailField(blank=True, default='', max_length=100, null=True),
        ),
    ]

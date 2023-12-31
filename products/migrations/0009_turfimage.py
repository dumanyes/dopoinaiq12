# Generated by Django 4.2.6 on 2023-10-29 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_timeslot_selected'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurfImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='turf_images/')),
                ('turf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.turf')),
            ],
        ),
    ]

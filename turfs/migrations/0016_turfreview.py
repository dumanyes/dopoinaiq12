# Generated by Django 4.2.6 on 2023-11-01 17:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turfs', '0015_alter_booking_turf_owner_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurfReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('review_text', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('turf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='turfs.turf')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 3.1.3 on 2021-04-14 11:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carparks', '0007_carparks_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='carparks',
            name='latitude',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carparks',
            name='longitude',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carparks',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]

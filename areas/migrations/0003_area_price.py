# Generated by Django 5.1.2 on 2024-10-18 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0002_area_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]

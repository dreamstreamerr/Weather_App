# Generated by Django 5.2 on 2025-04-27 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0003_drink_description_drink_image_drink_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]

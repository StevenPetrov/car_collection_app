# Generated by Django 4.1.2 on 2022-10-30 10:39

import car_collection_app.car_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0002_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.FloatField(validators=[car_collection_app.car_app.models.car_price_validator]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(validators=[car_collection_app.car_app.models.age_validate]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=10, validators=[car_collection_app.car_app.models.name_len_validator]),
        ),
    ]

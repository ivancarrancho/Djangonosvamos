# Generated by Django 2.1.1 on 2018-11-15 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_trip_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='price',
            field=models.PositiveSmallIntegerField(verbose_name='precio'),
        ),
    ]

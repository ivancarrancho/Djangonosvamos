# Generated by Django 2.1.1 on 2018-11-15 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20181104_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='price',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='precio'),
        ),
    ]

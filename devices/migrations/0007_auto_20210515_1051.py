# Generated by Django 3.1.5 on 2021-05-15 09:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0006_auto_20210428_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='date',
            field=models.DateField(default=datetime.date(2021, 5, 15)),
        ),
        migrations.AlterField(
            model_name='alert',
            name='time',
            field=models.TimeField(default=datetime.time(9, 50, 39, 151057)),
        ),
    ]
# Generated by Django 2.0.2 on 2018-03-15 22:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0006_auto_20180315_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget_pos',
            name='booking_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 15, 23, 35, 1, 664194)),
        ),
    ]

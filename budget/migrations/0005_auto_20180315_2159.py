# Generated by Django 2.0.2 on 2018-03-15 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_auto_20180315_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget_pos',
            name='booking_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 15, 21, 59, 48, 286862)),
        ),
    ]
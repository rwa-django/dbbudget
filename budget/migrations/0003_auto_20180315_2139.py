# Generated by Django 2.0.2 on 2018-03-15 20:39

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_auto_20180315_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget_pos',
            name='booking_booked',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='budget_pos',
            name='booking_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 15, 21, 39, 21, 207547)),
        ),
    ]

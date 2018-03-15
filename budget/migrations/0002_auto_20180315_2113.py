# Generated by Django 2.0.2 on 2018-03-15 20:13

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='login',
            field=models.CharField(default=2, help_text='Login', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='budget',
            name='budget_booked',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='budget_pos',
            name='booking_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 15, 21, 12, 27, 665200)),
        ),
    ]

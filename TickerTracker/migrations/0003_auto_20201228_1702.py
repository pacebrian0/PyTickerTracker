# Generated by Django 3.1.4 on 2020-12-28 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TickerTracker', '0002_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='lastRun',
            field=models.DateField(default=datetime.datetime(1, 1, 1, 0, 0), verbose_name='DateLastRun'),
        ),
    ]
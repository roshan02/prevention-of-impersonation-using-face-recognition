# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='ODE',
            field=models.BooleanField(default=False),
        ),
    ]
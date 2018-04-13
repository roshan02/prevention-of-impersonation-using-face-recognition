# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('DSA', models.BooleanField(default=False)),
                ('DLD', models.BooleanField(default=False)),
                ('DSGT', models.BooleanField(default=False)),
                ('SLS', models.BooleanField(default=False)),
            ],
        ),
    ]
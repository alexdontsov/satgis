# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-31 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20180831_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rasterdata',
            name='date',
            field=models.DateTimeField(max_length=255, verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='rasterlayer',
            name='date',
            field=models.DateTimeField(max_length=255, verbose_name='Time'),
        ),
    ]
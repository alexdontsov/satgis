# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-20 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20180820_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='metering',
            name='dataSource',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app.DataSource'),
            preserve_default=False,
        ),
    ]
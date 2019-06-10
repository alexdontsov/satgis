# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-09 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20190609_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='', max_length=1),
            preserve_default=False,
        ),
    ]
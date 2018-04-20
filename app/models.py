# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class WaterObject(models.Model):
    title = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    long = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.filename

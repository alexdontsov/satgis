# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models

class Shapefile(models.Model):
    filename = models.CharField(max_length=255)
    srs_wkt = models.CharField(max_length=255)
    geom_type = models.CharField(max_length=255)

class Attribute(models.Model):
    shapefile = models.ForeignKey(Shapefile)
    name = models.CharField(max_length=255)
    type = models.IntegerField()
    width = models.IntegerField()
    precision = models.IntegerField()

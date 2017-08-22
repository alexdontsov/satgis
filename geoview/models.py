from __future__ import unicode_literals

from django.contrib.gis.db import models

class RegionBorder(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

   # Returns the string representation of the model.
    def __str__(self):              # __unicode__ on Python 2
        return self.name

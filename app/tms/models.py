from django.contrib.gis.db import models

class BaseMap(models.Model):
    name = models.CharField(max_length=50)
    geometry = models.MultiPolygonField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return self.name

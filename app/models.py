# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class WaterObject(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    lat = models.CharField(max_length=255)
    long = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True)

    def __unicode__(self):
        return self.title

    def save(self):
        self.slug = '{0}-{1}'.format(self.pk, slugify(self.title))  # Статья будет отображаться в виде NN-АА-АААА
        super(WaterObject, self).save()

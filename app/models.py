# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.datetime_safe import datetime
from slugify import slugify
from import_export import resources



class WaterObject(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    lat = models.CharField(max_length=255)
    long = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True)

    def __unicode__(self):
        return self.title

    def save(self):
        self.slug = '{0}-{1}'.format(self.pk, slugify(self.title))
        super(WaterObject, self).save()


class Param(models.Model):
    type = models.CharField(verbose_name='Параметр', max_length=255)


class Metering(models.Model):
    value = models.CharField(verbose_name='Значение', max_length=255)
    waterObject = models.ForeignKey(WaterObject)
    type = models.ForeignKey(Param)
    time = models.CharField(verbose_name='Время', max_length=255)


class MeteringResource(resources.ModelResource):

    class Meta:
        model = Metering
        exclude = ('id',)
        import_id_fields = ('time',)
        skip_unchanged = True
        fields = ('time', 'value', 'type', 'waterObject')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from slugify import slugify
from import_export import resources


class WaterObject(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    lat = models.CharField(max_length=255)
    long = models.CharField(max_length=255)
    x1 = models.CharField(max_length=255)
    y1 = models.CharField(max_length=255)
    x2 = models.CharField(max_length=255)
    y2 = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True)
    slug_name = models.CharField(verbose_name='Slug', max_length=200, blank=True)

    def __unicode__(self):
        return self.title

    def save(self):
        self.slug = '{0}-{1}'.format(self.pk, slugify(self.title))
        super(WaterObject, self).save()

    class Meta:
        verbose_name = 'Водные объекты'
        verbose_name_plural = 'Водные объекты'


class Param(models.Model):
    type = models.CharField(verbose_name='Параметр', max_length=255)

    class Meta:
        verbose_name = 'Параметры'
        verbose_name_plural = 'Параметры'

    def __unicode__(self):
        return self.type


class ValueEd(models.Model):
    valueEd = models.CharField(verbose_name='Единицы измерения', max_length=255)

    class Meta:
        verbose_name = 'Единицы измерения'
        verbose_name_plural = 'Единицы измерения'

    def __unicode__(self):
        return self.valueEd

class DataSource(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    isEcspedit = models.BooleanField(verbose_name='Экспедиция')

    class Meta:
        verbose_name = 'Источники данных'
        verbose_name_plural = 'Источники данных'

    def __unicode__(self):
        return self.title


class Metering(models.Model):
    value = models.CharField(verbose_name='Значение', max_length=255)
    desc = models.CharField(verbose_name='Описание', max_length=255)
    waterObject = models.ForeignKey(WaterObject, verbose_name='Водный объект',)
    type = models.ForeignKey(Param, verbose_name='Параметр',)
    valueEd = models.ForeignKey(ValueEd, verbose_name='Единицы измерения',)
    dataSource = models.ForeignKey(DataSource, verbose_name='Источник данных',)
    time = models.DateTimeField(verbose_name='Время', max_length=255)
    lat = models.CharField(verbose_name='Широта', max_length=255)
    long = models.CharField(verbose_name='Долгота', max_length=255)

    class Meta:
        verbose_name = 'Измерения параметров'
        verbose_name_plural = 'Измерения параметров'
        ordering = ['-time']

    def __unicode__(self):
        return self.value + '|' + self.type.type + '|' + self.waterObject.title


class MeteringResource(resources.ModelResource):

    class Meta:
        model = Metering
        exclude = ('id',)
        import_id_fields = ('time', 'type', 'waterObject', 'dataSource')
        skip_unchanged = True
        fields = ('time', 'value', 'type', 'waterObject', 'dataSource')


class Article(models.Model):
    class Meta:
        ordering = ['-add_date']

    title = models.CharField(verbose_name='Заголовок', max_length=200)
    add_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    upd_date = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)
    text = models.TextField(verbose_name="Текст статьи", blank=True)
    slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True)

    def __unicode__(self):
        return self.title

    def save(self):
        self.slug = '{0}-{1}'.format(self.pk, slugify(self.title))  # Статья будет отображаться в виде NN-АА-АААА
        super(Article, self).save()

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class RasterData(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    product_id = models.CharField(verbose_name='ID', max_length=200)
    waterObject = models.ForeignKey(WaterObject)
    date = models.DateTimeField(verbose_name='Time', max_length=255)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Загруженные данные'
        verbose_name_plural = 'Загруженные данные'

class RasterLayer(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    product_id = models.CharField(verbose_name='ID', max_length=200)
    file = models.CharField(verbose_name='Файл', max_length=200)
    waterObject = models.ForeignKey(WaterObject)
    date = models.DateTimeField(verbose_name='Time', max_length=255)
    type = models.CharField(verbose_name='Тип', max_length=512)
    param = models.CharField(verbose_name='Параметр', max_length=512)

    def __unicode__(self):
        return self.title + '|' + self.waterObject.title

    class Meta:
        verbose_name = 'Слои данных'
        verbose_name_plural = 'Слои данных'


class VectorLayer(RasterLayer):
    class Meta:
        verbose_name = 'Векторные данные'
        verbose_name_plural = 'Векторные данные'
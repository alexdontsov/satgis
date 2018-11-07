# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import WaterObject, MeteringResource, Metering, Param, Article, DataSource, RasterLayer, RasterData
from import_export.admin import ImportExportModelAdmin

class MeteringAdmin(ImportExportModelAdmin):
    resource_class = MeteringResource



admin.site.register(WaterObject)
admin.site.register(Param)
admin.site.register(Article)
admin.site.register(DataSource)
admin.site.register(RasterLayer)
admin.site.register(RasterData)
admin.site.register(Metering, MeteringAdmin)





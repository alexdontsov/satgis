# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import WaterObject, MeteringResource, Metering, Param, Article, DataSource, RasterLayer, RasterData, ValueEd, Task, Algorithm, TaskAdmin
from import_export.admin import ImportExportModelAdmin

class MeteringAdmin(ImportExportModelAdmin):
    list_filter = ('time', 'waterObject', 'dataSource', 'type')
    list_display = ('value', 'type', 'time', 'waterObject')
    resource_class = MeteringResource



admin.site.register(Task, TaskAdmin)
admin.site.register(Algorithm)
admin.site.register(WaterObject)
admin.site.register(Param)
admin.site.register(ValueEd)
admin.site.register(Article)
admin.site.register(DataSource)
admin.site.register(RasterLayer)
admin.site.register(RasterData)
admin.site.register(Metering, MeteringAdmin)





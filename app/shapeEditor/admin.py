# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis import admin

from app.models import Metering
from .models import  *

from import_export import resources

admin.site.register(Shapefile, admin.ModelAdmin)
admin.site.register(Feature, admin.GeoModelAdmin)
admin.site.register(Attribute, admin.ModelAdmin)
admin.site.register(AttributeValue, admin.ModelAdmin)


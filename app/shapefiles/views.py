# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from app.shapeEditor.models import Shapefile

def list_shapefiles (request):
    shapefiles = Shapefile.objects.all().order_by('filename')
    return render(request, "list_shapefiles.html" ,
                  { 'shapefiles' : shapefiles })

def import_shapefile (request):
    return HttpResponse("Продолжение с л ед у е т ..." )
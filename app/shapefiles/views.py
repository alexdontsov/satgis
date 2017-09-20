# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from app.shapeEditor.models import Shapefile
from django.http import HttpResponseRedirect
from forms import ImportShapefileForm

def list_shapefiles (request):
    shapefiles = Shapefile.objects.all().order_by('filename')
    return render(request, "list_shapefiles.html" ,
                  { 'shapefiles' : shapefiles })

def import_shapefile (request):
    if request.method == "GET":
        form = ImportShapefileForm()
        return render(request, "import_shapefile.html", {'form': form})
    elif request.method == "POST":
        form = ImportShapefileForm(request.POST, request.FILES)
        if form. is_valid():
            shapefile = request.FILES['import_file']
            # Продолжение с л е д у е т ...
            return HttpResponseRedirect("/")
        return render(request, "import_shapefile.html", {'form' : form})
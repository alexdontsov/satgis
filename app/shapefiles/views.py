# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from app.shapeEditor.models import Shapefile
from django.http import HttpResponseRedirect
from .forms import ImportShapefileForm
from django.shortcuts import render_to_response
import shapefileIO

def list_shapefiles (request):
    shapefiles = Shapefile.objects.all().order_by('filename')
    return render(request, "list_shapefiles.html" ,
                  { 'shapefiles' : shapefiles })

def import_shapefile(request):
    if request.method == "GET":
        form = ImportShapefileForm()
        return render(request, "import_shapefile.html",
                      {'form': form,
                       'errMsg': None})
    elif request.method == "POST":
        errMsg = None # initially.

        form = ImportShapefileForm(request.POST,
                                   request.FILES)
        if form.is_valid():
            shapefile = request.FILES['import_file']
            errMsg = shapefileIO.import_data(shapefile)
            if errMsg == None:
                return HttpResponseRedirect("/")

        return render(request, "import_shapefile.html",
                      {'form': form,
                       'errMsg': errMsg})

'''
export data
'''
def export_shapefile(request, shapefile_id):
  try:
    shapefile = Shapefile.objects.get(id=shapefile_id)
  except Shapefile.DoesNotExist:
    raise Http404('File not found')

  return shapefileIO.export_data(shapefile)
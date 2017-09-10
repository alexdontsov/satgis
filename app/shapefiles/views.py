# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def list_shapefiles (request):
    return HttpResponse("ответ из функции list_ sh a p efiles" )

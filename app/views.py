# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from .models import WaterObject

def all_waterobjects(request):
    articles = WaterObject.objects.all()
    return render_to_response('all_waters.html', {'articles': articles}, context_instance=RequestContext(request))

def one_waterobject_by_slug(request, slug):
    article = get_object_or_404(WaterObject, slug=slug)
    return render(request, 'one_article.html', {'article': article}, context_instance=RequestContext(request))


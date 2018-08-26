# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from wms.views import WmsView

from app.wmsmap import MyWmsView
from .models import WaterObject, Article, Metering


def all_waterobjects(request):
    articles = WaterObject.objects.all()
    return render_to_response('all_waters.html', {'articles': articles})

def one_waterobject_by_slug(request, slug):

    article = get_object_or_404(WaterObject, slug=slug)
    meterings = Metering.objects.select_related().filter(waterObject = article.id)
    if meterings:
        return render(request, 'water_obj_data.html', {'article': article, 'meterings': meterings})

    return render(request, 'water_obj.html', {'article': article})

def all_articles(request):
    articles = Article.objects.all()
    return render_to_response('all_articles.html', {'articles': articles})

def one_article_by_slug(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'article.html', {'article': article})


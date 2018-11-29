# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, get_object_or_404
from .models import WaterObject, Article, Metering, RasterLayer
from django.conf import settings




def all_waterobjects(request):
    articles = WaterObject.objects.all()
    return render_to_response('all_waters.html', {'articles': articles})

def one_waterobject_by_slug(request, slug):

    article = get_object_or_404(WaterObject, slug=slug)
    meterings = Metering.objects.select_related().filter(waterObject=article.id).order_by('-time')
    layers = RasterLayer.objects.select_related().filter(waterObject=article.id).order_by('-date')

    project_path = settings.BASE_DIR
    return render(request, 'water_obj.html',
                    {'water_obj': article, 'layers': layers, 'project_path': project_path, 'meterings': meterings}
                  )

def all_articles(request):
    articles = Article.objects.all()
    return render_to_response('all_articles.html', {'articles': articles})

def one_article_by_slug(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'article.html', {'article': article})


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response, get_object_or_404
from .models import WaterObject, Article, Metering, RasterLayer, Param
from django.conf import settings


def all_waterobjects(request):
    articles = WaterObject.objects.all()
    return render_to_response('all_waters.html', {'articles': articles})


def one_waterobject_by_slug(request, slug):
    article = get_object_or_404(WaterObject, id=slug)
    chart_display = False
    chart_title = ''
    chart_param = ''

    layers = RasterLayer.objects.select_related().filter(waterObject=article.id).order_by('-date')
    params = Param.objects.all()

    meterings = Metering.objects.select_related().filter(waterObject=article.id).order_by('-time')

    page = request.GET.get('page', '')

    if request.GET.get('param', '') and request.GET.get('param', '') != '0':
        meterings = meterings.filter(type=request.GET.get('param', ''))

        if meterings:
            chart_title = meterings[0].type
            chart_param = meterings[0].type

    if request.GET.get('date_from', ''):
        meterings = meterings.filter(time__gte=request.GET.get('date_from', ''))

    if request.GET.get('date_to', ''):
        meterings = meterings.filter(time__lte=request.GET.get('date_to', ''))

    if request.GET.get('chart_display', ''):
        chart_display = True

    project_path = settings.BASE_DIR

    paginator = Paginator(meterings, 12)

    try:
        meterings = paginator.page(page)
    except PageNotAnInteger:
        meterings = paginator.page(1)
    except EmptyPage:
        meterings = paginator.page(paginator.num_pages)

    return render(request, 'water_obj.html',
          {
              'water_obj': article,
              'layers': layers,
              'project_path': project_path,
              'meterings': meterings,
              'params': params,
              'chart_display': chart_display,
              'chart_title': chart_title,
              'chart_param': chart_param,
           }
        )

def all_articles(request):
    articles = Article.objects.all()
    return render_to_response('all_articles.html', {'articles': articles})

def one_article_by_slug(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'article.html', {'article': article})


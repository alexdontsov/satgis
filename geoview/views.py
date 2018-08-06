from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
# from ModestMaps.Core import Coordinate
# from TileStache import getTile, parseConfigfile
# from TileStache.Core import KnownUnknown
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.sites.models import Site
# from utils import APIPermissionMixin
#######################################################################################################################
# Main page view
#######################################################################################################################
from app.models import Article


def index(request, template_name='index.html'):
    articles = Article.objects.all().order_by('-id')
    paginator = Paginator(articles, 2)
    page = request.GET.get('page')
    # articles = paginator.page(page)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, template_name, {'articles': articles})

def about(request, template_name='about.html'):
    return render(request, template_name)

def examples(request, template_name='examples.html'):
    return render(request, template_name)

def news(request, template_name='news.html'):
    return render(request, template_name)


# class TileManager(APIPermissionMixin, View):
#     """
#         Returns tiles
#     """
#     def get(self, request, *args, **kwargs):
#         try:
#             #the mixin already checked that the layers and users exist
#             user = User.objects.get(username__exact=kwargs['tile_user'])
#             config = parseConfigfile(user.get_profile().tile_config_file)
#             layer = config.layers[kwargs['tile_layer']]
#             coord = Coordinate(int(kwargs['tile_row']), int(kwargs['tile_column']), int(kwargs['tile_zoom']))
#             tile_mimetype, tile_content = getTile(layer, coord, kwargs['tile_format'], ignore_cached=False)
#             return HttpResponse(mimetype=tile_mimetype, content=tile_content)
#         except KnownUnknown, e:
#             return HttpResponseServerError(str(e))


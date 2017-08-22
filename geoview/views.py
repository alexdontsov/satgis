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

def index(request, template_name='index.html'):
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


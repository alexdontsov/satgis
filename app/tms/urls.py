from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',
        root), # "/tms" вызывает root()
    # url(r'^(?P<version>[0-9.]+)$',
    #     service), # напр., "/tms/1.0" вызывает service(version="1.0")
    # url(r'^(?P<version>[0-9.]+)/(?P<shapefile_id>\d+)$',
    #     tileMap), # напр., "/tms/1.0/2" вызывает
    #               # tileMap(version="1.0", shapefile_id=2)
    # url(r'^(?P<version>[0-9.]+)/' +
    #     r'(?P<shapefile_id>\d+)/(?P<zoom>\d+)/' +
    #     r'(?P<x>\d+)/(?P<y>\d+)\.png$',
    #     tile), # напр., "/tms/1.0/2/3/4/5" вызывает
    #            # tile(version="1.0", shapefile_id=2, zoom=3, x=4, y=5)
]
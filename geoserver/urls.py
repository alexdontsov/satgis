from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.flatpages import views

from app import shapefiles
from app import tms
from app.shapefiles.views import list_shapefiles
from app.views import all_waterobjects, one_waterobject_by_slug

admin.site.site_header = ('SibWater 1.0')
admin.site.index_title = ('SibWater 1.0')
admin.site.site_title = ('Admin panel')

urlpatterns = [
    url(r'^', include('geoview.urls')),
    # url(r'^v1/tiles/(?P<tile_user>([^/]+))/(?P<tile_layer>([^/]+))/(?P<tile_zoom>(\d+))/(?P<tile_column>(\d+))/(?P<tile_row>(\d+))\.(?P<tile_format>([a-z]+))$', TileManager.as_view(), name='tile_manager'),
    url(r'^admin/', admin.site.urls),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^shape-files', list_shapefiles),
    url(r'^import', shapefiles.views.import_shapefile),
    url(r'^export/(?P<shapefile_id>\d+)$',
            shapefiles.views.export_shapefile),
    url(r'^tms/', include('app.tms.urls')),
    url(r'^waterobjects/$', all_waterobjects),
    url(r'^waterobjects/(?P<slug>[\w-]+)/$', one_waterobject_by_slug),

]

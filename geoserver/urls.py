from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.flatpages import views

from app import shapefiles
from app import tms
from app.shapefiles.views import list_shapefiles
from app.views import all_waterobjects, one_waterobject_by_slug, one_article_by_slug, WmsView
from app.wmsmap import MyWmsView

admin.site.site_header = ('SibWater 1.0')
admin.site.index_title = ('SibWater 1.0')
admin.site.site_title = ('Admin panel')

urlpatterns = [
    url(r'^', include('geoview.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^shape-files', list_shapefiles),
    url(r'^import', shapefiles.views.import_shapefile),
    url(r'^export/(?P<shapefile_id>\d+)$',
            shapefiles.views.export_shapefile),
    url(r'^tms/', include('app.tms.urls')),
    url(r'^waterobjects/$', all_waterobjects),
    url(r'^waterobjects/(?P<slug>[\w-]+)/$', one_waterobject_by_slug),
    url(r'^news/(?P<slug>[\w-]+)/$', one_article_by_slug),
    url(r'^wms/$', MyWmsView.as_view(), name='wms'),

]

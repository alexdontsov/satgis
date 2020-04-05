from django.conf.urls import url
from django.views.static import serve

from geoserver import settings
from .views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^media/(?P<path>.*)',serve, {'document_root':settings.MEDIA_ROOT},name='img'),
    url(r'^news', news, name='news'),
    url(r'^examples', examples, name='examples'),
    url(r'^about', about, name='about'),
]

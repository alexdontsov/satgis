from django.conf.urls import url
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    # url(r'^news', news, name='news'),
    url(r'^examples', examples, name='examples'),
    url(r'^about', about, name='about'),
]

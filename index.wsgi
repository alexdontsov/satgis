# -*- coding: utf-8 -*-

import os, sys, site

activate_this = '/home/d/dcorpsoftw/.venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
site.addsitedir('/home/d/dcorpsoftw/.venv/lib/python2.7/site-packages')
sys.path.insert(1,'/home/d/dcorpsoftw/satgis.ru/')

import django

if django.VERSION[1] <= 6:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'geoserver.settings'
    import django.core.handlers.wsgi
    application = django.core.handlers.wsgi.WSGIHandler()
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geoserver.settings")
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()


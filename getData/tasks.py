from __future__ import absolute_import, unicode_literals
from celery import shared_task
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date

#http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#using-custom-scheduler-classes
@shared_task
def getSentinelData(login, pass, obj):
    api = SentinelAPI('rumato', '123qweR$', 'https://scihub.copernicus.eu/dhus')
    footprint = geojson_to_wkt(read_geojson('nvd.geojson'))
    products = api.query(footprint,
                        date = ('NOW-13DAYS', 'NOW'),
                        platformname = 'Sentinel-2',
                        cloudcoverpercentage = (0, 30)
                )

    # api.download_all(products)
    print products

    # api.to_geodataframe(products)

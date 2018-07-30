from __future__ import absolute_import, unicode_literals
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from app.models import RasterData

# http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#using-custom-scheduler-classes
# @app.task(bind=True)
def getSentinelData():
    # login, pass, obj
    api = SentinelAPI('rumato', '123qweR$', 'https://scihub.copernicus.eu/dhus')
    footprint = geojson_to_wkt(read_geojson('nvd.geojson'))
    products = api.query(footprint,
                         date=('NOW-13DAYS', 'NOW'),
                         platformname='Sentinel-2',
                         cloudcoverpercentage=(0, 30)
                         )
    for product_id, product in products.items():
        print product_id, product
        # assert isinstance(product_id, object)
        p = RasterData(title=product_id, product_id=product_id)
        p.save()

        exit()

    api.download_all(products)
    # return products
    # api.download('d833db51-85fe-4242-9bb2-e7b129d0b117')
    # api.to_geodataframe(products)


getSentinelData()

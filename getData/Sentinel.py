from __future__ import absolute_import, unicode_literals
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from app.models import RasterData
import zipfile
import os

from osgeo import gdal

# http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#using-custom-scheduler-classes
# @app.task(bind=True)
'''
example command: python manage.py getsentinel --date=NOW-2DAYS --geojson=/home/alex/DCORP/SatGis/satgis/getData/nvd.geojson --platformname=Sentinel-2
'''


def getSentinelData(geojson, date='NOW-2DAYS', platformname='Sentinel-2', cloudcoverpercentage=(0, 30)):
    # login, pass, obj
    api = SentinelAPI('rumato', '123qweR$', 'https://scihub.copernicus.eu/dhus')
    # footprint = geojson_to_wkt(read_geojson('/home/alex/DCORP/SatGis/satgis/getData/nvd.geojson'))
    footprint = geojson_to_wkt(read_geojson(geojson))
    products = api.query(footprint,
                         date=(date, 'NOW'),
                         platformname=platformname,
                         cloudcoverpercentage=cloudcoverpercentage
                         )
    for product_id, product in products.items():

        if RasterData.objects.filter(product_id=product_id).exists():
            print 'data in db...product_id = ' + product_id + ' ---> ' + product['title']
            #
        else:
            print 'get data... product_id = ' + product_id + ' ---> ' + product['title']

            api.download(product_id)
            p = RasterData(title=product['title'], product_id=product_id)
            p.save()
            zip = zipfile.ZipFile(product['title'] + '.zip')
            zip.extractall('./rasters')
            zip.close()
            os.remove(product['title'] + '.zip')
            '''
            open rasters
            '''
            patch = './rasters/' + product['title'] + '.SAFE/GRANULE/'
            f = os.listdir(patch)
            patch = patch + f[0] + '/IMG_DATA/'
            files = os.listdir(patch)
            os.makedirs('./rasters/' + product['title'])
            print files
            for file in files:
                if 'xml' not in file:
                    ds = gdal.Open(patch + file)
                    ds = gdal.Translate('./rasters/' + product['title'] + '/' + file, ds,
                                        projWin=[571377.923077, 6067937.5, 609733.615385, 6021562.5])
                    ds = None
                    '''
                    /home/alex/DCORP/SatGis/satgis/rasters/S2A_MSIL1C_20180819T054641_N0206_R048_T44UNF_20180819T075215/
                    T44UNF_20180816T053641_B02.jp2 /home/alex/DCORP/SatGis/satgis/rasters/S2A_MSIL1C_20180819T054641_N0206_R048_T44UNF_20180819T075215/b1.tif
                    '''
                    transform_file = file.split('.')
                    transform_file = transform_file[0] + '.tif'
                    '''
                    gdalwarp -overwrite -s_srs EPSG:32644 -t_srs EPSG:4326 -of GTiff /home/alex/DCORP/SatGis/satgis/rasters/S2A_MSIL1C_20180816T053641_N0206_R005_T44UNF_20180816T083341.SAFE/GRANULE/L1C_T44UNF_A016447_20180816T053640/
                    IMG_DATA/T44UNF_20180816T053641_B04.jp2 /home/alex/DCORP/SatGis/
                    satgis/rasters/S2A_MSIL1C_20180816T053641_N0206_R005_T44UNF_20180816T083341/test.tif
                    '''
                    os.system(
                        'gdalwarp -overwrite -s_srs EPSG:32644 -t_srs EPSG:4326 -of GTiff ' + './rasters/' + product['title'] + '/' + file
                        + '  ./rasters/' + product['title'] + '/' + transform_file)

                    # delete jp2
                    os.remove('./rasters/' + product['title'] + '/' + file)

            print 'calc NDWI indes for ' + product['title']
            indexNDWI(product)
            # delete data
            # os.remove('./rasters/' + product['title'] + '.SAFE')
        # exit()

    # api.download_all(products)
    # return products
    # api.download('d833db51-85fe-4242-9bb2-e7b129d0b117')
    # api.to_geodataframe(products)


def indexNDWI(product):
    command = 'gdal_calc.py -A ./rasters/' + product['title'] + '/*_B04.tif ' \
                  '-B ./rasters/' \
              + product['title'] + '/*_B08.tif --outfile=./rasters/' + product['title'] + '/' + 'ndwi.tif --calc="(A-B)/(A+B)"'
    os.system(command)

def createComposite(product):
    command = 'gdal_calc.py -A ./rasters/' + product['title'] + '/*_B04.tif ' \
                  '-B ./rasters/' \
              + product['title'] + '/*_B08.tif --outfile=./rasters/' + product['title'] + '/' + 'ndwi.tif --calc="(A-B)/(A+B)"'
    os.system(command)
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import datetime
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from app.models import RasterData, WaterObject, RasterLayer, VectorLayer
import zipfile
import os

from osgeo import gdal
from django.utils import timezone
import pytz


# http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#using-custom-scheduler-classes
# @app.task(bind=True)
'''
example command: python manage.py getsentinel --date=NOW-2DAYS --geojson=/home/alex/DCORP/SatGis/satgis/getData/nvd.geojson 
--platformname=Sentinel-2 --waterObject=nwdh
'''


def getSentinelData(geojson, waterObject, date='NOW-2DAYS', platformname='Sentinel-2', cloudcoverpercentage=(0, 30)):
    # login, pass, obj
    api = SentinelAPI('rumato', '123qweR$', 'https://scihub.copernicus.eu/dhus')
    # footprint = geojson_to_wkt(read_geojson('/home/alex/DCORP/SatGis/satgis/getData/nvd.geojson'))
    footprint = geojson_to_wkt(read_geojson(geojson))
    products = api.query(footprint,
                         date=(date, 'NOW'),
                         platformname=platformname,
                         cloudcoverpercentage=cloudcoverpercentage
                         )
    waterObj = WaterObject.objects.get(slug_name=waterObject)
    print waterObj
    # print waterObj.x1

    timezone.now()
    # exit()
    for product_id, product in products.items():

        if RasterData.objects.filter(product_id=product_id).exists():
            print 'data in db...product_id = ' + product_id + ' ---> ' + product['title']
            #
        else:
            print 'get data... product_id = ' + product_id + ' ---> ' + product['title']

            api.download(product_id)
            print product['ingestiondate']
            # exit()
            p = RasterData(title=product['title'], product_id=product_id, waterObject=waterObj,
                           date=product['ingestiondate'])
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
            for file in files:
                if 'xml' not in file:

                    # ds = gdal.Open(patch + file)
                    # ds = gdal.Translate('./rasters/' + product['title'] + '/' + file, ds,
                    #                     projWin=[571377.923077, 6067937.5, 609733.615385, 6021562.5])
                    # ds = None

                    print 'gdal_translate -of GTiff -a_nodata 0 -projwin '+ waterObj.x1 +', '+ waterObj.y1+', '+ waterObj.x2+', '+ waterObj.y2+'   ' + patch + file + ' ./rasters/' + product['title'] + '/' + file

                    os.system(
                        'gdal_translate -of GTiff -a_nodata 0 -projwin '+ waterObj.x1 +' '+ waterObj.y1 +' '+ waterObj.x2 +' '+ waterObj.y2 +'  '
                        + patch + file
                        + ' ./rasters/' + product['title'] + '/' + file)

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
                        'gdalwarp  -overwrite -s_srs EPSG:32644 -t_srs EPSG:4326 -of GTiff ' + './rasters/' + product['title'] + '/' + file
                        + '  ./rasters/' + product['title'] + '/' + transform_file)

                    # delete jp2
                    os.remove('./rasters/' + product['title'] + '/' + file)

            print 'calc NDWI indes for ' + product['title']
            indexNDWI(product)
            ############
            l = RasterLayer(title=product['title'], product_id=product_id, waterObject=waterObj,
                           date=product['ingestiondate'],
                           file=product['title'] + '/' + 'ndwi.tif', type='raster', param='NDWI индекс')
            l.save()
            #### natural color
            createComposite(product)
            l = RasterLayer(title=product['title'], product_id=product_id, waterObject=waterObj,
                            date=product['ingestiondate'],
                            file=product['title'] + '/' + 'natural.tif', type='raster', param='Комбинация каналов 4-3-2')
            l.save()
            ### vector
            '''
            gdal_polygonize.py /home/alex/DCORP/SatGis/satgis/rasters/S2B_MSIL1C_20180920T053639_N0206_R005_T44UNF_20180920T081720/ndwi.tif -f "ESRI Shapefile" 
            /home/alex/DCORP/SatGis/satgis/rasters/S2B_MSIL1C_20180920T053639_N0206_R005_T44UNF_20180920T081720/temp.shp temp DN=0
            '''
            os.system(
                'gdal_polygonize.py ' + './rasters/' + product['title'] + '/ndwi-t.tif -f "ESRI Shapefile" ' + './rasters/' + product['title'] + '/temp.shp temp DN=0')

            '''
            ogr2ogr -f "ESRI Shapefile" -dialect SQLite -sql 'SELECT *,ST_Area(geometry) AS area FROM temp ORDER BY area DESC LIMIT 1' test1.shp temp.shp
            '''
            os.system(
                'ogr2ogr -f "ESRI Shapefile" -dialect SQLite -sql "SELECT *,ST_Area(geometry) AS area FROM temp ORDER BY area DESC LIMIT 1"'
                ' ./rasters/' + product['title'] + '/ndwi.shp  ./rasters/' + product['title'] + '/temp.shp ')

            vector = VectorLayer(title=product['title'], product_id=product_id, waterObject=waterObj,
                            date=product['ingestiondate'],
                            file=product['title'] + '/' + 'ndwi.shp', type='vector', param='NDWI')
            vector.save()
            # delete data
            # os.remove('./rasters/' + product['title'] + '.SAFE')
        # exit()

    # api.download_all(products)
    # return products
    # api.download('d833db51-85fe-4242-9bb2-e7b129d0b117')
    # api.to_geodataframe(products)

'''
("T44UPF_20180918T054631_B04@1"-"T44UPF_20180918T054631_B08@1")/("T44UPF_20180918T054631_B04@1"+"T44UPF_20180918T054631_B08@1")
'''
def indexNDWI(product):
    command = 'gdal_calc.py -A ./rasters/' + product['title'] + '/*_B04.tif ' \
                  '-B ./rasters/' + product['title'] + '/*_B08.tif --outfile=./rasters/'\
              + product['title'] + '/' + 'ndwi-t.tif --calc="(A-B)/(A+B)"'
    print command

    os.system(command)

    command = 'gdal_translate -scale -ot Byte ./rasters/' + product['title'] + '/ndwi-t.tif ./rasters/' + product['title'] + '/ndwi.tif -a_nodata 0'
    print command

    os.system(command)


'''
gdal_merge.py -n 0 -a_nodata 0 -separate -of Gtiff -o natural.tif  *_B04.tif  *_B03.tif  *_B02.tif
'''
def createComposite(product):

    command = 'gdal_merge.py -n 0 -a_nodata 0 -separate -of Gtiff -o ./rasters/' + product['title'] + '/natural-t.tif ' \
                  './rasters/' + product['title'] + '/*_B04.tif ./rasters/' + product['title'] + '/*_B03.tif ./rasters/'\
              + product['title'] + '/*_B02.tif'
    print command

    os.system(command)

    command = 'gdal_translate -ot Byte -scale 0 4096 0 255 -b 1 -b 2 -b 3 -a_nodata 0 ./rasters/' + product['title'] + '/natural-t.tif ./rasters/' + product['title'] + '/natural.tif'
    print command

    os.system(command)
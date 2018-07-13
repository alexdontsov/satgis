# from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
# from datetime import date
#
# api = SentinelAPI('rumato', '123qweR$', 'https://scihub.copernicus.eu/dhus')
# footprint = geojson_to_wkt(read_geojson('nvd.geojson'))
# products = api.query(footprint,
#                     date = ('NOW-13DAYS', 'NOW'),
#                     platformname = 'Sentinel-2',
#                     cloudcoverpercentage = (0, 30)
#                      )
#
# api.download_all(products)
# print products

# api.to_geodataframe(products)

import zipfile

'''
unzip
'''
zip = zipfile.ZipFile('S2B_MSIL1C_20180622T053639_N0206_R005_T44UNF_20180622T084445.zip')
zip.extractall()
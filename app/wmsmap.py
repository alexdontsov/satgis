from wms import maps, layers, views
from raster.models import RasterTile
from wms.layers import WmsRasterLayer

mycartograpy = [
    {
        'name': 'Category A',
        'expression': '1',
        'color': '0 0 255'
    },
    {
        'name': 'Category B',
        'expression': '2',
        'color': '255 0 0'
    }
]

class MyRasterLayer(WmsRasterLayer):
    model = RasterTile
    where="filename=\\\home/alex/DCORP/SatGis/satgis/rasters/S2A_MSIL1C_20180816T053641_N0206_R005_T44UNF_20180816T083341/ndwi.tif\\\'"
    nodata = '0'
    cartography = mycartograpy

class MyWmsMap(maps.WmsMap):
    layer_classes = [MyRasterLayer]

class MyWmsView(views.WmsView):
    map_class = MyWmsMap
    slug = None
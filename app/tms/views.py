# -*- coding: utf-8 -*-
import math
import traceback
import mapnik

from django.conf import settings
from django.http import HttpResponse
from django.http import Http404

from ..shapeEditor.models import Shapefile
from ..shapeEditor import utils

MAX_ZOOM_LEVEL = 10
TILE_WIDTH     = 256
TILE_HEIGHT    = 256

def root(request):
    try:
        baseURL = request.build_absolute_uri()
        xml = []
        xml.append('<?xml version="1.0" encoding="utf-8" ?>')
        xml.append('<Services>')
        xml.append('  <TileMapService ' +
                   'title="Служба TMS приложения ShapeEditor" ' +
                   'version="1.0" href="' + baseURL + '1.0"/>')
        xml.append('</Services>')
        response = "\n".join(xml)
        return HttpResponse(response, content_type="text/xml")
    except:
        traceback.print_exc()
        return HttpResponse("Ошибка")


def service(request, version):
    try:
        # if version != "1.0":
        #     raise Http404

        baseURL = request.build_absolute_uri()
        xml = []
        xml.append('<?xml version="1.0" encoding="utf-8" ?>')
        xml.append('<TileMapService version="1.0" services="' +
                   baseURL + '">')
        xml.append('<Title>Служба TMS приложения ShapeEditor' +
                   '</Title>')
        xml.append('  <Abstract></Abstract>')
        xml.append('  <TileMaps>')
        for shapefile in Shapefile.objects.all():
            id = str(shapefile.id)
            xml.append('<TileMap title="' +
                       shapefile.filename + '"')
            xml.append('             srs="EPSG:4326"')
            xml.append('             href="'+baseURL+'/'+id+'"/>')
        xml.append('  </TileMaps>')
        xml.append('</TileMapService>')
        # response = "\n".join(xml)
        response = xml
        return HttpResponse(response, content_type="text/xml")
    except:
        traceback.print_exc()
        return HttpResponse("Ошибка")



def _unitsPerPixel(zoomLevel):
    return 0.703125 / math.pow(2, zoomLevel)


def tileMap(request, version, shapefile_id):
    if version != "1.0":
        raise Http404

    try:
        shapefile = Shapefile.objects.get(id=shapefile_id)
    except Shapefile.DoesNotExist:
        raise Http404

    try:
        baseURL = request.build_absolute_uri()
        xml = []
        xml.append('<?xml version="1.0" encoding="utf-8" ?>')
        xml.append('<TileMap version="1.0" ' +
                   'tilemapservice="' + baseURL + '">')
        xml.append('  <Title>' + shapefile.filename + '</Title>')
        xml.append('  <Abstract></Abstract>')
        xml.append('  <SRS>EPSG:4326</SRS>')
        xml.append('  <BoundingBox minx="-180" miny="-90" ' +
                   'maxx="180" maxy="90"/>')
        xml.append('  <Origin x="-180" y="-90"/>')
        xml.append('  <TileFormat width="' + str(TILE_WIDTH) +
                   '" height="' + str(TILE_HEIGHT) + '" ' +
                   'mime-type="image/png" extension="png"/>')
        xml.append('  <TileSets profile="global-geodetic">')
        for zoomLevel in range(0, MAX_ZOOM_LEVEL+1):
            href = baseURL + "/{}".format(zoomLevel)
            unitsPerPixel = "{}".format(_unitsPerPixel(zoomLevel))
            order = "{}".format(zoomLevel)

            xml.append('    <TileSet href="' + href + '" ' +
                       'units-per-pixel="'+  unitsPerPixel + '"' +
                       ' order="' + order + '"/>')
        xml.append('  </TileSets>')
        xml.append('</TileMap>')
        response = "\n".join(xml)
        return HttpResponse(response, content_type="text/xml")
    except:
        traceback.print_exc()
        return HttpResponse("Ошибка")


#############################################################################

def tile(request, version, shapefile_id, zoom, x, y):
    try:
        # Разобрать и проверить параметры.
        if version != "1.0":
            raise Http404

        try:
            shapefile = Shapefile.objects.get(id=shapefile_id)
        except Shapefile.DoesNotExist:
            raise Http404

        zoom = int(zoom)
        x = int(x)
        y = int(y)

        if zoom < 0 or zoom > MAX_ZOOM_LEVEL:
            raise Http404

        xExtent = _unitsPerPixel(zoom) * TILE_WIDTH
        yExtent = _unitsPerPixel(zoom) * TILE_HEIGHT

        minLong = x * xExtent - 180.0
        minLat = y * yExtent - 90.0
        maxLong = minLong + xExtent
        maxLat = minLat + yExtent

        if (minLong < -180 or maxLong > 180 or
                minLat < -90 or maxLat > 90):
            raise Http404

        # Задать базовый слой и слой геообъектов.
        map_string = '''<?xml version="1.0" encoding="utf-8"?>
<Map background-color="#7391ad" srs="+proj=longlat +datum=WGS84">
    <FontSet name="bold-fonts">
        <Font face-name="DejaVu Sans Bold" />
    </FontSet>

    <Style name="baseLayerStyle">
        <Rule>
            <PolygonSymbolizer fill="#b5d19c" />
            <LineSymbolizer stroke="#404040" stroke-width="0.2" />
        </Rule>
    </Style>

    <Style name="featureLayerStyle">
        <Rule>
		    <!--(Symbolizers)-->
        </Rule>
    </Style>

    <Layer name="baseLayer">
        <StyleName>baseLayerStyle</StyleName>
        <Datasource>
            <Parameter name="type">postgis</Parameter>
            <Parameter name="user">(User)</Parameter>
            <Parameter name="password">(Password)</Parameter>
            <Parameter name="dbname">(Dbname)</Parameter>
            <Parameter name="table">tms_basemap</Parameter>
            <Parameter name="geometry_field">geometry</Parameter>
            <Parameter name="geometry_table">tms_basemap</Parameter>
            <Parameter name="srid">4326</Parameter>
        </Datasource>
    </Layer>

    <Layer name="featureLayer">
        <StyleName>featureLayerStyle</StyleName>
        <Datasource>
            <Parameter name="type">postgis</Parameter>
            <Parameter name="user">(User)</Parameter>
            <Parameter name="password">(Password)</Parameter>
            <Parameter name="dbname">(Dbname)</Parameter>
            <Parameter name="table">(Query)</Parameter>
            <Parameter name="geometry_field">(Geometry_field)</Parameter>
            <Parameter name="geometry_table">shared_feature</Parameter>
            <Parameter name="srid">4326</Parameter>
        </Datasource>	
    </Layer>
</Map>
'''
        # Получить инфо о БД.
        dbSettings = settings.DATABASES['default']
        user = dbSettings['USER']
        passwd = dbSettings['PASSWORD']
        dbname = dbSettings['NAME']

        geometry_field = utils.calc_geometry_field(shapefile.geom_type)

        query = '(select ' + geometry_field \
                + ' from "shared_feature" where' \
                + ' shapefile_id=' + str(shapefile.id) + ') as geom'

        symbolizer = ""

        if shapefile.geom_type in ["Point", "MultiPoint"]:
            symbolizer = '<PointSymbolizer />'
        elif shapefile.geom_type in ["LineString", "MultiLineString"]:
            symbolizer = '<LineSymbolizer stroke="#000000" stroke-width="0.5" />'
        elif shapefile.geom_type in ["Polygon", "MultiPolygon"]:
            symbolizer = '<PolygonSymbolizer fill="#f7edee" /><LineSymbolizer stroke="#000000" stroke-width="0.5" />'

        # Выполнить подстановку
        map_string = map_string.replace("(User)", user)
        map_string = map_string.replace("(Password)", passwd)
        map_string = map_string.replace("(Dbname)", dbname)
        map_string = map_string.replace("(Geometry_field)", geometry_field)
        map_string = map_string.replace("(Query)", query)
        map_string = map_string.replace("<!--(Symbolizers)-->", symbolizer)

        # Настроить карту.
        gmap = mapnik.Map(TILE_WIDTH, TILE_HEIGHT)
        mapnik.load_map_from_string(gmap, map_string)
        # В заключение визуализировать сегмент.
        # gmap.zoom_to_box(mapnik.Envelope(minX, minY, maxX, maxY))
        gmap.zoom_to_box(mapnik.Box2d(minLong, minLat, maxLong, maxLat))
        image = mapnik.Image(TILE_WIDTH, TILE_HEIGHT)
        mapnik.render(gmap, image)
        imageData = image.tostring('png')

        return HttpResponse(imageData, content_type="image/png")
    except:
        traceback.print_exc()
        return HttpResponse("Ошибка")

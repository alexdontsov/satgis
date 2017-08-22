#!/bin/sh
# USAGE: . get_landsat_composite.sh <LANDSAT_SCENE_ID>
scene=${1}

for (( band=1; band<=8; band++ ))
do
    gdal_translate -a_nodata 0 -co COMPRESS=LZW ${scene}_B${band}.TIF b${band}.tif
done 

var baseLayer = new ol.layer.Group({
    'title': '',
    layers: [
new ol.layer.Tile({
    'title': 'OSM',
    'type': 'base',
    source: new ol.source.OSM()
})
]
});


var format_proby0 = new ol.format.GeoJSON();
var features_proby0 = format_proby0.readFeatures(json_proby0,
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_proby0 = new ol.source.Vector({
    attributions: [new ol.Attribution({html: '<a href=""></a>'})],
});
jsonSource_proby0.addFeatures(features_proby0);
var lyr_proby0 = new ol.layer.Vector({
                source:jsonSource_proby0,
                style: style_proby0,
                title: "Слой имерений"
            });

lyr_proby0.setVisible(true);
lyr_proby0.set('fieldAliases', { 'desc': 'desc'});
lyr_proby0.set('fieldImages', {'desc': 'TextEdit' });
lyr_proby0.set('fieldLabels', {'desc': 'no label' });
lyr_proby0.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});



var xyz = new ol.layer.Tile({
 opacity: 1,
                            title: "Проверка",
            source: new ol.source.XYZ({
              url: '/raster/tiles/2/{z}/{x}/{y}.png'
            })
          });


//var lyr_crop0 = new ol.layer.Image({
//                            opacity: 1,
//                            title: "Sentinel-2  ",
//
//
//                            source: new ol.source.ImageStatic({
//                               url: "/static/layers/crop0.png",
//    attributions: [new ol.Attribution({html: '<a href=""></a>'})],
//                                projection: 'EPSG:3857',
//                                alwaysInRange: true,
//                                //imageSize: [5977, 7823],
//                                imageExtent: [9187051.373466, 7235021.370650, 9294060.487381, 7367369.020618]
//                            })
//                        });
//
//lyr_crop0.setVisible(true);


var lyr_NDCI0 = new ol.layer.Image({
                            opacity: 1,
                            title: "Индекс NDCI",


                            source: new ol.source.ImageStatic({
                               url: "/static/layers/NDCI0.png",
    attributions: [new ol.Attribution({html: '<a href=""></a>'})],
                                projection: 'EPSG:3857',
                                alwaysInRange: true,
                                //imageSize: [10980, 10980],
                                imageExtent: [9186915.839951, 7179726.993326, 9382070.677117, 7362400.085412]
                            })
                        });

lyr_NDCI0.setVisible(true);

var layersList = [baseLayer,  xyz];

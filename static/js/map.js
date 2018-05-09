var geojson = {
"type": "FeatureCollection",
"features": [
{ "type": "Feature", "properties": { "id": "1", "desc": "Боровое - Быстровка, л.б.", "value": 10.62 + ' мг/м3'}, "geometry": { "type": "Point", "coordinates": [ 82.65654255225229, 54.684554714785996 ] } },
{ "type": "Feature", "properties": { "id": "2", "desc": "Боровое - Быстровка, середина", "value": 8.70 + ' мг/м3' }, "geometry": { "type": "Point", "coordinates": [ 82.701112830012292, 54.670203960687608 ] } },
{ "type": "Feature", "properties": { "id": "3", "desc": "Боровое - Быстровка, п.б.", "value": 7.81 + ' мг/м3' }, "geometry": { "type": "Point", "coordinates": [ 82.759294390202015, 54.655848133832556 ] } },
{ "type": "Feature", "properties": { "id": "4", "desc": "Бердский залив, Агролес", "value": 82.35 + ' мг/м3' }, "geometry": { "type": "Point", "coordinates": [ 83.133204325182646, 54.766164809822932 ] } },
{ "type": "Feature", "properties": { "id": "5", "desc": "Бердский залив, Речкуновка" , "value": 11.78 + ' мг/м3'}, "geometry": { "type": "Point", "coordinates": [ 83.073021105812145, 54.783521380488686 ] } },
{ "type": "Feature", "properties": { "id": "6", "desc": "Верхний бьеф (у плотины)" , "value": 16.41 + ' мг/м3'}, "geometry": { "type": "Point", "coordinates": [ 82.982145779002082, 54.844767819748363 ] } },
{ "type": "Feature", "properties": { "id": "6", "desc": "Ленинское - Сосновка, л.б." , "value": 22.07 + ' мг/м3'}, "geometry": { "type": "Point", "coordinates": [ 82.863013696755814, 54.807581196099548 ] } },
{ "type": "Feature", "properties": { "id": "7", "desc": "Ленинское - Сосновка, середина" , "value": 15.16 + ' мг/м3'}, "geometry": { "type": "Point", "coordinates": [ 82.919593929600836, 54.767877707240167 ] } },
{ "type": "Feature", "properties": { "id": "8", "desc": "Ленинское - Сосновка, п.б." , "value": 14.66 + ' мг/м3'}, "geometry": { "type": "Point", "coordinates": [ 82.986849678076993, 54.727518755049267 ] } }
]
};


var conf = {
    base: {
        title: 'Базовые слои',
        layers: [
            {
                group: "Внешние сервисы",
                collapsed: true,
                layers: [
                	{
                		name: "OpenStreetMap",
                		active: true,
                		layer:  L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	                                maxZoom: 19,
	                            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
                        })
                	},
                    {
                        name: "OpenTopoMap",
                        layer: L.tileLayer('http://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
	                            maxZoom: 17,
	                            attribution: 'Map data: &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
                        })
                    },
                    {
                        name: "Esri.WorldImagery",
                        layer: L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
	                            attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
                            })
                    }

                ]
            },
            {
                group: "###############",
                layers: [

                    {
                        name: "Land Cover 2009",
                        layer: {
                            type: "tileLayer",
                            args: [
                                "https://s3.amazonaws.com/wri-tiles/global-landcover/{z}/{x}/{y}.png", {
                                    attribution: "<a href='http://earthenginepartners.appspot.com/science-2013-global-forest'>Maps land cover distribution globally</a>",
                                    maxZoom: 12
                                }
                            ]
                        }
                    }
                ]
            }
        ]
    },
    tree: {
        title: "#########################",
        layers: [
                {
                        name: "Sentinel-2, 29.08.2017",
                        layer: {
                            type: "tileLayer.wms",
                            args: [
                                "http://localhost/cgi-bin/mapserv?map=/var/www/html/map.map&", {
                                    maxZoom: 12,
                                    format: 'image/png',
				                    transparent: true,
                                    layers: 'test',
                                    crs: L.CRS.EPSG4326,
                                    version: '1.1.1',
                                }
                            ]
                        }
                    },

                 {
                        name: "Sentinel-2, NDCI индекс, 29.08.2017",
                        layer: {
                            type: "tileLayer.wms",
                            args: [
                                "http://localhost/cgi-bin/mapserv?map=/var/www/html/map.map&", {
                                    maxZoom: 12,
                                    format: 'image/png',
				                    transparent: true,
                                    layers: 'ndci',
                                    crs: L.CRS.EPSG4326,
                                    version: '1.1.1',
                                }
                            ]
                        }
                    },

                    {
                        name: "Sentinel-2, NDCI индекс, 29.08.2017",
                        layer: {
                            type: "geoJson",
                            args: [
                                geojson,
                                {
    style: function(feature) {
        return {
        	color: "red"
        };
    },
    pointToLayer: function(feature, latlng) {
        return new L.CircleMarker(latlng, {
        	radius: 7,
        	fillOpacity: 0.85
        });
    },
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.desc +'<br>' + '<b>' + feature.properties.value + '<b>');
    }
}
                            ]
                        }
                    },

        ]
    }
};


var map = L.map('map', {
        center: L.latLng([52.46, 82.37]),
        zoom: 6
    });

var base1 = L.control.panelLayers(conf.base.layers, null,  {
    title: conf.base.title,
	position: 'topright',
	compact: true
}).addTo(map);



var over1 = L.control.panelLayers(null, conf.tree.layers, {
    title: conf.tree.title,
    position: 'topright',
    compact: true
}).addTo(map);


var scale = L.control.scale().addTo(map);

map.on('zoomend', function() {
    var y = map.getSize().y,
        x = map.getSize().x;
    // calculate the distance the one side of the map to the other using the haversine formula
    var maxMeters = map.containerPointToLatLng([0, y]).distanceTo( map.containerPointToLatLng([x,y]));
    // calculate how many meters each pixel represents
    var MeterPerPixel = maxMeters/x ;
    // say this is your scale
    // This is the scale denominator
    console.log('scale denominator: ',MeterPerPixel*scale.options.maxWidth);

    console.log('zoom', map.getZoom() )
});

geojsonLayer = L.geoJson(geojson, {
    style: function(feature) {
        return {
        	color: "red"
        };
    },
    pointToLayer: function(feature, latlng) {
        return new L.CircleMarker(latlng, {
        	radius: 7,
        	fillOpacity: 0.85
        });
    },
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.desc +'<br>' + '<b>' + feature.properties.value + '<b>');
    }
});

//map.addLayer(geojsonLayer);


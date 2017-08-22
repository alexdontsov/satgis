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
                        name: "Landscape",
                        layer: {
                            type: "tileLayer",
                            args: [
                                "http://{s}.tile3.opencyclemap.org/landscape/{z}/{x}/{y}.png"
                            ]
                        }
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
                        name: "Landsat оз. Красиловское (30.07.2016)",
                        layer: {
                            type: "tileLayer",
                            args: [
                                "/static/tiles/landsat/{z}/{x}/{y}.png", {
                                    maxZoom: 12,
                                    tms:true
                                }
                            ]
                        }
                    },
            {
                active: false,
                name: "Gain",
                layer: {
                    type: "tileLayer",
                    args: [
                        "http://earthengine.google.org/static/hansen_2013/gain_alpha/{z}/{x}/{y}.png", {
                        	maxZoom: 12,
        					attribution:
        					'<a href="http://earthenginepartners.appspot.com/science-2013-global-forest"> '+
        					'Tree Cover Gain (12 years, 30m, global)</a>'
                        }
                    ]
                }
            },
            {
                name: "Loss",
                layer: {
                    type: "tileLayer",
                    args: [
                        "http://earthengine.google.org/static/hansen_2013/loss_alpha/{z}/{x}/{y}.png", {
                        	maxZoom: 12,
        					attribution:
        					'<a href="http://earthenginepartners.appspot.com/science-2013-global-forest"> '+
        					'Tree Cover Loss (12 years, 30m, global)</a>'
                        }
                    ]
                }
            }
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

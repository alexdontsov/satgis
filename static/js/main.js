var trace1 = {
  x: dataChartX,
  y: dataChartY,
  type: 'scatter'
};

console.log(trace1)

let layout = {
        title: "Площадь",
        font: { size: 19 },
        width: 800,
        height: 450,
        xaxis: {
            autorange: true,
            type: 'time',
            title: 'time',
            showgrid: true,
            showline: true,
            tickformat: '%d.%m.%Y',

        },
        yaxis: {
            autorange: true,
            type: 'linear',
            title: '',
            showgrid: true,
            showline: true,
            automargin: true,
        }
    };

var data = [trace1];

Plotly.newPlot('chart1', data, layout, {responsive: true, displaylogo: false});

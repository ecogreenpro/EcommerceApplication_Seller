var options = {
    series: [{
        name: 'series1',
        data: [100, 120, 99, 125, 127, 130, 148]
    }],
    chart: {
        height: 350,
        type: 'area',
        toolbar: {
            show: false
        }
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        curve: 'smooth'
    },
    colors: ['#fcb800', '#f9f9f9', '#9C27B0'],
    xaxis: {
        type: 'datetime',
        categories: [
            '2020-09-19T00:00:00.000Z',
            '2020-09-20T00:00:00.000Z',
            '2020-09-21T00:00:00.000Z',
            '2020-09-22T00:00:00.000Z',
            '2020-09-23T00:00:00.000Z',
            '2020-09-24T00:00:00.000Z',
            '2020-09-25T00:00:00.000Z',
        ]
    },
    tooltip: {
        x: {
            format: 'dd/MM/yy HH:mm'
        },
    },

};

var donutChart  = {
    series: [22, 37, 41],
    chart: {
        height: '250',
        type: 'donut'
    },
    chartOptions: {
        labels: ['Apple', 'Mango', 'Orange']
    },

    plotOptions: {
        pie: {
            donut: {
                size: '71%',
                polygons: {
                    strokeWidth: 0
                }
            },
            expandOnClick: false
        }
    },
    states: {
        hover: {
            filter: {
                type: 'darken',
                value: 0.9
            }
        }
    },

    dataLabels: {
        enabled: false
    },

    legend: {
        show: false
    },
    tooltip: {
        enabled: false
    }
};

var donut = new ApexCharts(document.querySelector("#donut-chart"), donutChart);
donut.render();

var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();




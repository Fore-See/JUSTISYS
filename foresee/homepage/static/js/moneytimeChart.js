// $(function () {
function show_moneytime_chart() {
    $('.moneytimeChart').highcharts({

        chart: {
            type: 'scatter',
            zoomType: 'xy',
            // width: 450,
            height: 300,
            spacingBottom: 0,
            spacingTop: 5,
            spacingLeft: 0,
            spacingRight: 0,
            backgroundColor: '#fff',
            // borderColor: '#EBBA95',
            // borderWidth: 2
        },
        credits: {
            enabled: false
        },
        exporting: {
            enabled: false
        },
        title: {
            text: '判決金額與時間分布圖',
            style: {
                fontSize: '20px',
                fontFamily: 'Microsoft JhengHei, Verdana, sans-serif',
            }
        },

        xAxis: {
            title: {
                enabled: true,
                text: '歷時(日)'
            },
            startOnTick: true,
            endOnTick: true,
            showLastLabel: true
        },
        yAxis: {
            title: {
                text: '判<br>決<br>金<br>額<br>(NT)',
                rotation:0
            }
        },
        // legend: {
        //     enabled:false,
        //     layout: 'vertical',
        //     align: 'left',
        //     verticalAlign: 'top',
        //     x: 100,
        //     y: 70,
        //     floating: true,
        //     backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#eee',
        //     borderWidth: 1
        // },
        plotOptions: {
            scatter: {
                marker: {
                    radius: 5,
                    states: {
                        hover: {
                            enabled: true,
                            lineColor: 'rgb(100,100,100)'
                        }
                    }
                },
                states: {
                    hover: {
                        marker: {
                            enabled: false
                        }
                    }
                },
                tooltip: {
                    headerFormat: '<b>{series.name}</b><br>',
                    // pointFormat: '判決名稱'
                    // pointFormat: '判決名稱<br>{point.x} 日, {point.y} 元'
                    pointFormat: '{point.x} 日, {point.y} 元'
                }
            }
        },
        series: [{
            name: '小額',//可以貼判決名稱
            color: 'rgba(223, 83, 83, .5)',
            data: moneytime['小額']

        }, {
            name: '簡易',
            color: 'rgba(95, 223, 132, .5)',
            data: moneytime['簡易']
        }, {
            name: '普通',
            color: 'rgba(80, 91, 223, .5)',
            data: moneytime['普通']
        }, {
            name: '保險',
            color: 'rgba(223, 196, 108, .5)',
            data: moneytime['保險']
        }]
    });
};


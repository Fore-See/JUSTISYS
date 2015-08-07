$("#chart").click(function() {
    // $('#ChartSec').css({visibility: 'visible'});
        $('#container6').highcharts({
        chart: {
            type: 'pie',
            width: 400,
            spacingBottom: 3,
            spacingTop: 40,
            spacingLeft: 0,
            spacingRight: 0
        },
        title: {
            text: '勝敗機率',
                style: {
                    fontSize: '20px'}
        },
        series: [{
            data: [30,70],
            dataLabels: {
                format: '{y}'/*'{point.y}'*/
            }
        }]
    });

    // button handler
    var chart = $('#container6').highcharts(),
        x = 0,
        y = 0;
    $('#total').click(function () {
        x = 30;
        y = 70;
        chart.series[0].data[0].update(x);
        chart.series[0].data[1].update(y);
    });   
    $('#lawyer').click(function () {
        x = 40;
        y = 60;
        chart.series[0].data[0].update(x);
        chart.series[0].data[1].update(y);
    });
    $('#docs').click(function () {
        x = 50;
        y = 50;
        chart.series[0].data[0].update(x);
        chart.series[0].data[1].update(y);
    });
    $('#arg').click(function () {
        x = 10;
        y = 90;
        chart.series[0].data[0].update(x);
        chart.series[0].data[1].update(y);
    });
});
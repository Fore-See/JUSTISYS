// $("#chart").click(function() {
// $(function() {
function show_win_chart() {
    // console.log('win: '+win_lose['win']);
    // console.log('lose: '+win_lose['lose']);
    $('.winChart').highcharts({
        chart: {
            type: 'pie',
            width: 450,
            spacingBottom: 20,
            spacingTop: 5,
            spacingLeft: 0,
            spacingRight: 0,
            backgroundColor: '#eee'
        },

        credits: {
            enabled: false
        },

        exporting: {
            enabled: false
        },

        title: {
            text: '勝敗比例',
                style: {
                    fontSize: '15px',
                    fontFamily: 'Microsoft JhengHei, Verdana, sans-serif',
                }
        },

        series: [{
            data: [win_lose['win'], win_lose['lose']],
            dataLabels: {
                format: '{y}'/*'{point.y}'*/
            },
        }]
    });

    // button handler
    var chart = $('.winChart').highcharts(),
        x = 0;
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
};
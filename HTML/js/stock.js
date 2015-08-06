// $("#chart").click(function() {
$(document).ready(function() {
    var options = {
        chart: {
            renderTo: 'container1',
            type: 'spline',
            width: 700,
            spacingBottom: 0,
            spacingTop: 0,
            spacingLeft: 0,
            spacingRight: 0,

        },
        series: [{}]
    };
    
    var src =  "http://www.highcharts.com/samples/data/jsonp.php?filename=aapl-ohlcv.json&callback=?";
    $.getJSON(src,  function(data) {
        options.series[0].data = data;
        var chart = new Highcharts.Chart(options);
    });
});
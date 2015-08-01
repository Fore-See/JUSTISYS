$(document).ready(function() {
    var options = {
        chart: {
            renderTo: 'container',
            type: 'spline'
        },
        series: [{}]
    };
    
    var src =  "http://www.highcharts.com/samples/data/jsonp.php?filename=aapl-ohlcv.json&callback=?";
    $.getJSON(src,  function(data) {
        options.series[0].data = data;
        var chart = new Highcharts.Chart(options);
    });
});
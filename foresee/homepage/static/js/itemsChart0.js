// $("#chart").click(function() {
// $(function() {
function show_item_chart() {
    // console.log(chartitem);
    $('.itemsChart').highcharts({
        chart: {
            type: 'column',
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
            text: '求償項目',
                style: {
                        fontSize: '15px',
                        fontFamily: 'Microsoft JhengHei, Verdana, sans-serif',
                }
        },
        xAxis: {
            type: 'category',
            labels: {
                rotation: -45,/*橫軸項目名稱傾斜角度*/
                style: {
                    fontSize: '12px',
                    fontFamily: 'Microsoft JhengHei, Verdana, sans-serif',
                }
            }
        },
        yAxis: {
            min: 0,            
            title: {
                text: '比例或次數 (millions)',
                style: {
                    fontSize: '12px',
                    fontFamily: 'Microsoft JhengHei',
                }
            }
        },
        legend: {
            enabled: false
            /*改變"比例或次數"的值上限，ture是150，flase是125，但我搞不懂差異@@*/
        },
        tooltip: {
            pointFormat: '框框裡的字 2008: <b>{point.y:.1f} millions</b>'
        },
        series: [{
            name: '比例或次數',/*圖表名稱*/
            data: chartitem,
            dataLabels: {
                enabled: true,/*柱狀圖上的數字*/
                rotation: -20,/*柱狀圖上的數字旋轉角度*/
                color: '#FFFFFF',/*柱狀數字的顏色*/
                align: 'right',
                format: '{y}', // '{point.y:.1f}'= one decimal
                y: 10, // 10 pixels down from the top
                style: {
                    fontSize: '15px',
                    fontFamily: 'Microsoft JhengHei, Verdana, sans-serif'
                }
            }/*end of dataLabels*/
        }]/*end of series*/
    });
};
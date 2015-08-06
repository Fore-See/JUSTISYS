$("#chart").click(function() {

    $('#container5').highcharts({

        chart: {
            type: 'columnrange',
            inverted: true, /*控制縱橫，false是直的柱子*/
            width: 660,
            spacingBottom: 3,
            spacingTop: 130,
            spacingLeft: 0,
            spacingRight: 0
        },

        title: {
            text: 'Temperature variation by month'
        },

        subtitle: {
            text: 'Observed in Vik i Sogn, Norway'
        },

        xAxis: {
            categories: ['小額', '簡易', '普通', '保險']
        },/*end of xAxis*/

        yAxis: {
            title: {
                text: '時間 ( 日 )'
            }
        },/*end of yAxis，數值是跟著data range自動跑的*/

        tooltip: {
            valueSuffix: '小框框裡的單位'
        },

        plotOptions: {
            columnrange: {
                dataLabels: {
                    enabled: true,/*顯示兩端點數值的開關*/
                    formatter: function () {
                        return this.y + '日';
                    }
                }
            }
        },/*end of plotOptions*/

        legend: {
            enabled: true/*關閉圖表的開關*/
        },/*end of legend*/

        series: [{
            name: '歷時統計',/*圖表打開或跳出浮框才會看到這個*/
            data: [
                [255,665],
                [452, 872],
                [531, 975],
                [314, 751]                
            ]/*end of data*/
        }]/*end of series*/

    });/*end of highCharts*/

});/*end of function*/
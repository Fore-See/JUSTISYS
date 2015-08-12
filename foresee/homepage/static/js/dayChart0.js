// $("#chart").click(function() {
// $(function() {
function show_day_chart() {
    $('.dayChart').highcharts({
        chart: {
            type: 'columnrange',
            inverted: true, /*控制縱橫，false是直的柱子*/
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
            text: '歷時統計',
                style: {
                        fontSize: '15px',
                        fontFamily: 'Microsoft JhengHei, Verdana, sans-serif',
                }
        },

        xAxis: {
            categories: ['小額', '簡易', '普通', '保險'],
            labels: {
                style: {
                    fontSize: '12px',
                    fontFamily: 'Microsoft JhengHei',
                }
            }
        },/*end of xAxis*/

        yAxis: {
            title: {
                text: '時間 ( 日 )',
                    style: {
                        fontSize: '12px',
                        fontFamily: 'Microsoft JhengHei'
                    }
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
                        return this.y;
                    }
                }
            }
        },/*end of plotOptions*/

        legend: {
            enabled: false,/*關閉圖表的開關*/
            itemStyle: {
                fontSize: '12px',
                fontFamily: 'Microsoft JhengHei'
            }
        },/*end of legend*/

        series: [{
            name: '歷時分佈',/*圖表打開或跳出浮框才會看到這個*/
            data: [
                dayrange['小額'],
                dayrange['簡易'],
                dayrange['普通'],
                dayrange['保險'],                
            ]/*end of data*/
        }]/*end of series*/

    });/*end of highCharts*/

};/*end of function*/
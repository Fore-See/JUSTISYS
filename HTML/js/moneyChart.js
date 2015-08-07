$("#chart").click(function() {

    $('#container3').highcharts({

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
            text: '賠償金額範圍'
        },

        subtitle: {
            text: '金額分佈'
        },

        xAxis: {
            categories: ['小額', '簡易', '普通', '保險'],
            labels: {
                style: {
                    fontSize: '20px',
                    fontFamily: 'Microsoft JhengHei',
                    fontWeight: 'bold'
                }
            }
        },/*end of xAxis*/

        yAxis: {
            title: {
                text: '金額 ( 元 )'
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
                        return this.y + '元';
                    }
                }
            }
        },/*end of plotOptions*/

        legend: {
            enabled: false,/*關閉圖表的開關*/
            itemStyle: {
                fontSize: '20px',
                fontFamily: 'Microsoft JhengHei'
            }
        },/*end of legend*/

        series: [{
            name: '金額分布',/*圖表打開或跳出浮框才會看到這個*/
            data: [
                [1000,207798],
                [1063, 6039030],
                [1000, 98487190],
                [458, 89313548]               
            ],/*end of data*/  

            dataLabels: {
            format: '{point.y:,.0f}'
            }

        }]/*end of series*/

    });/*end of highCharts*/

});/*end of function*/
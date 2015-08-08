// $("#chart").click(function() {
// $(function() {
function show_money_chart() {
    $('.moneyChart').highcharts({
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
            text: '判賠金額分佈',
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
            name: '金額分佈',/*圖表打開或跳出浮框才會看到這個*/
            data: [
                damagerange['小額'],
                damagerange['簡易'],
                damagerange['普通'],
                damagerange['保險'],
            ]/*end of data*/
            // data: [
            //     [20000,45000],
            //     [57000, 350000],
            //     [150000, 975000],
            //     [40000, 490000]                
            // ]
        }]/*end of series*/

    });/*end of highCharts*/

};/*end of function*/
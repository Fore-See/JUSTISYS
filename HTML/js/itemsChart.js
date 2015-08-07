$("#chart").click(function() {
    $('#container4').highcharts({
        chart: {
            type: 'column',
            width: 800,
            spacingBottom: 3,
            spacingTop: 10,
            spacingLeft: 0,
            spacingRight: 0
        },
        title: {
            text: '賠償項目',
            style: {
                fontSize: '30px',
                fontFamily: 'Verdana, sans-serif'
            }


        },
        // subtitle: {
        //     text: 'Source: <a href="http://en.wikipedia.org/wiki/List_of_cities_proper_by_population">Wikipedia</a>'
        // },
        xAxis: {
            type: 'category',
            labels: {
                rotation: -45,/*橫軸項目名稱傾斜角度*/
                style: {
                    fontSize: '20px',
                    fontFamily: 'Microsoft JhengHei, Verdana, sans-serif',
                    fontWeight: 'bold'
                }
            }
        },
        yAxis: {
            min: 0,            
            title: {
                text: '比例或次數 (millions)',
                style: {
                    fontSize: '15px',
                    fontFamily: 'Verdana, sans-serif'
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
            data: [
                ['精神慰撫金',200],
                ['維修費',40],
                ['醫療費',35],
                ['後續調養費',22],
                ['膳食費',57],
                ['交通費',84],
                ['看護費',46],
                ['勞動能力損失',75],
                ['薪資補償費',71],
                ['殯葬費',91],
                ['撫養費',19],
                ['撫恤金',57],
                ['財產損失',54],
                ['生活費用',28],
                ['拖車費',37],
                ['剩餘殘值',69]
            ],
            dataLabels: {
                enabled: true,/*柱狀圖上的數字*/
                rotation: -20,/*柱狀圖上的數字旋轉角度*/
                color: '#FFFFFF',/*柱狀數字的顏色*/
                align: 'right',
                format: '{y}', // '{point.y:.1f}'= one decimal
                y: 10, // 10 pixels down from the top
                style: {
                    fontSize: '13px',
                    fontFamily: 'Verdana, sans-serif'
                }
            }/*end of dataLabels*/
        }]/*end of series*/
    });
});
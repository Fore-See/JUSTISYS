// $("#chart").click(function() {
// $(function() {
function show_win_chart() {
    // Highcharts.setOptions({
    //     colors: ['#ff6bb4', '#76bdff']
    // });
    // console.log('win: '+win_lose['win']);
    // console.log('lose: '+win_lose['lose']);
    $('.winChart').highcharts({
        
        chart: {
            type: 'pie',
            // width: 450,
            height: 250,
            spacingBottom: 0,
            spacingTop: 5,
            spacingLeft: 0,
            spacingRight: 0,
            backgroundColor: '#fff',
            // borderColor: '#EBBA95',
            // borderWidth: 2
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
                    fontSize: '20px',
                    fontFamily: 'Microsoft JhengHei, Verdana, sans-serif',
                }
        },
        tooltip: {
            pointFormat: '{point.y} %',
            // valueSuffix: ' cm',
            // shared: true
        },
// input two int count(win) count(loss)
// colors: ['#ff6bb4', '#76bdff'],
         series: [{//   y  為預設####################
            name: "",
            colorByPoint: false,
            data: [{
                name: "敗訴",
                y: Math.round((win_lose['ni_nl_nd'][1]*100)/verdictnums),
                color:'#ff6bb4'
            }, {
                name: "勝訴",
                y: Math.round((win_lose['ni_nl_nd'][0]*100)/verdictnums),
                sliced: true,
                selected: true,//外圍有沒有薄框
                color:'#76bdff'
            }]
        }]
    });

    // button handler   
    var chart = $('.winChart').highcharts(),
        x = 0;
        y = 0;

    $('input[name="winchart"]').click(function(){
        if ($('#invesdoc').is(":checked")) {
            $('label[for="invesdoc"]').html('有證明文件');
        } else {
            $('label[for="invesdoc"]').html('沒有證明文件');
        }

        if ($('#lawyer').is(":checked")) {
            $('label[for="lawyer"]').html('原告有請律師');
        } else {
            $('label[for="lawyer"]').html('原告沒有請律師');
        }

        if ($('#dassertion').is(":checked")) {
            $('label[for="dassertion"]').html('被告有主張');
        } else {
            $('label[for="dassertion"]').html('被告沒有主張');
        }


        if ( $('#invesdoc').is(":checked") && $('#lawyer').is(":checked") && $('#dassertion').is(":checked") ) {
            x = Math.round((win_lose['wi_wl_wd'][1]*100)/verdictnums);
            y = Math.round((win_lose['wi_wl_wd'][0]*100)/verdictnums);
            $('.winChart').highcharts().series[0].data[0].update(x);
            $('.winChart').highcharts().series[0].data[1].update(y);        
            console.log('ok');
        }

        else if ( !($('#invesdoc').is(":checked")) && $('#lawyer').is(":checked") && $('#dassertion').is(":checked") ){
            x = Math.round((win_lose['ni_wl_wd'][1]*100)/verdictnums);
            y = Math.round((win_lose['ni_wl_wd'][0]*100)/verdictnums);
            $('.winChart').highcharts().series[0].data[0].update(x);
            $('.winChart').highcharts().series[0].data[1].update(y);        
            console.log('ok');
        }

        else if ( $('#invesdoc').is(":checked") && !($('#lawyer').is(":checked")) && $('#dassertion').is(":checked") ){
            x = Math.round((win_lose['wi_nl_wd'][1]*100)/verdictnums);
            y = Math.round((win_lose['wi_nl_wd'][0]*100)/verdictnums);
            $('.winChart').highcharts().series[0].data[0].update(x);
            $('.winChart').highcharts().series[0].data[1].update(y);        
            console.log('ok');
        }

        else if ( $('#invesdoc').is(":checked") && $('#lawyer').is(":checked") && !($('#dassertion').is(":checked")) ){
            x = Math.round((win_lose['wi_wl_nd'][1]*100)/verdictnums);
            y = Math.round((win_lose['wi_wl_nd'][0]*100)/verdictnums);
            $('.winChart').highcharts().series[0].data[0].update(x);
            $('.winChart').highcharts().series[0].data[1].update(y);        
            console.log('ok');
        }

        else if ( !($('#invesdoc').is(":checked")) && !($('#lawyer').is(":checked")) && $('#dassertion').is(":checked") ){
            x = Math.round((win_lose['ni_nl_wd'][1]*100)/verdictnums);
            y = Math.round((win_lose['ni_nl_wd'][0]*100)/verdictnums);
            $('.winChart').highcharts().series[0].data[0].update(x);
            $('.winChart').highcharts().series[0].data[1].update(y);        
            console.log('ok');
        }

        else if ( $('#invesdoc').is(":checked") && !($('#lawyer').is(":checked")) && !($('#dassertion').is(":checked")) ){
            x = Math.round((win_lose['wi_nl_nd'][1]*100)/verdictnums);
            y = Math.round((win_lose['wi_nl_nd'][0]*100)/verdictnums);
            $('.winChart').highcharts().series[0].data[0].update(x);
            $('.winChart').highcharts().series[0].data[1].update(y);        
            console.log('ok');
        }

        else if ( !($('#invesdoc').is(":checked")) && !($('#lawyer').is(":checked")) && !($('#dassertion').is(":checked")) ){
            x = Math.round((win_lose['ni_nl_nd'][1]*100)/verdictnums);
            y = Math.round((win_lose['ni_nl_nd'][0]*100)/verdictnums);
            $('.winChart').highcharts().series[0].data[0].update(x);
            $('.winChart').highcharts().series[0].data[1].update(y);        
            console.log('ok');
        }
        else {};
    });


};

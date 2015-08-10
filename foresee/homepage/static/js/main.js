$(function() {
// nothing
console.log("nothing")
// search_verdict();
// show_result();
// console.log('shortcut testing');
});

$(document).ready(function(){
    $('[data-toggle="tab"]').tooltip('show');
    $('[data-toggle="tooltip"]').tooltip();
});
$(document).click(function(){
    if ($('#search-form').hasClass('tabsection')){$('[data-toggle="tooltip"]').tooltip();
    } else if ($('#mychart, #verdicts').hasClass('resultsection')) {
        $('a[data-toggle="tooltip"]').attr('data-original-title', '未達搜尋條件');
        setTimeout(function(){
            $('a[data-toggle="tooltip"]').tooltip();
            $('a[href="#mytabs"]').tooltip('destroy');
        }, 200);
    };
    setTimeout(function(){
        if(! $('#mychart, #verdicts').hasClass('resultsection')) {
            $('a[data-toggle="tooltip"]').tooltip('destroy');
        };
    }, 1000);
});

// P or D button
$('#plaintiff').click(function(){
    $(this).addClass('custom-btn-hover');
    $('#defendant').removeClass('custom-btn-hover');
});
$('#defendant').click(function(){
    $(this).addClass('custom-btn-hover');
    $('#plaintiff').removeClass('custom-btn-hover');
});

// Submit search on submit
// $('#search-form').on('submit', function(event){
//     event.preventDefault();
//     console.log("form submitted!")  // sanity check
//     search_verdict();
// });

// Initialize variables for chart
var win_lose = {
    'ni_nl_nd': [0, 0],
    'wi_nl_nd': [0, 0],
    'ni_wl_nd': [0, 0],
    'ni_nl_wd': [0, 0],
    'wi_wl_nd': [0, 0],
    'wi_nl_wd': [0, 0],
    'ni_wl_wd': [0, 0],
    'wi_wl_wd': [0, 0],
};
var damageitemcount = {
    '維修費' : 0, '拖車費': 0, '交通費': 0, '精神慰撫金': 0, '醫療費': 0, 
    '勞動能力損失': 0, '看護費': 0, '薪資補償費': 0, '後續調養費': 0, 
    '財產損失': 0, '生活費用': 0, '撫養費': 0, '殯葬費': 0, '撫恤金': 0, 
    '膳食費': 0, '剩餘殘值': 0
};
var chartitem = [];
var damagelist = {'小額':[], '簡易':[], '普通':[], '保險':[]};
var daylist = {'小額':[], '簡易':[], '普通':[], '保險':[]};
var damagerange = {'小額':[], '簡易':[], '普通':[], '保險':[]};
var dayrange = {'小額':[], '簡易':[], '普通':[], '保險':[]};

// Reset value for chart
function reset() {
    win_lose = {
        'ni_nl_nd': [0, 0], 'wi_nl_nd': [0, 0], 'ni_wl_nd': [0, 0], 'ni_nl_wd': [0, 0], 
        'wi_wl_nd': [0, 0], 'wi_nl_wd': [0, 0], 'ni_wl_wd': [0, 0], 'wi_wl_wd': [0, 0],
    };
    damageitemcount = {
        '維修費' : 0, '拖車費': 0, '交通費': 0, '精神慰撫金': 0, '醫療費': 0, 
        '勞動能力損失': 0, '看護費': 0, '薪資補償費': 0, '後續調養費': 0, 
        '財產損失': 0, '生活費用': 0, '撫養費': 0, '殯葬費': 0, '撫恤金': 0, 
        '膳食費': 0, '剩餘殘值': 0
    };
    chartitem = [];
    damagelist = {'小額':[], '簡易':[], '普通':[], '保險':[]};
    daylist = {'小額':[], '簡易':[], '普通':[], '保險':[]};
    damagerange = {'小額':[], '簡易':[], '普通':[], '保險':[]};
    dayrange = {'小額':[], '簡易':[], '普通':[], '保險':[]};
};

// Click on P or D, display tab section
$('#plaintiff, #defendant').click(function(){
    $('#search-form').removeClass('tabsection');
    setTimeout(function(){
        $('.tomytabs').trigger('click');
    }, 200);
});

// Click on p_d
var p_d = '';
$('input[name="p_d"]').click(function(){
    $('input[name="p_d"]:checked').each(function(){
        p_d = $(this).val();
        console.log('p_d: ' + p_d);
    });
});

$('#plaintiff').click(function(){
    p_d = 'P';
    console.log('p_d: ' + p_d);
});

$('#defendant').click(function(){
    p_d = 'D';
    console.log('p_d: ' + p_d);
});

// Check Validation
function validation() {
    console.log('checking validation');
    if ( $('input[name="vehicle_me"]').is(":checked") && $('input[name="vehicle_them"]').is(":checked") && $('input[name="judge_situation"]').is(":checked")) {
        search_verdict();
        show_result();
        console.log('ok');
    };
};

// Click on vehicle_me
var vel_me = [];
$('input[name="vehicle_me"]').click(function(){
    vel_me = [];
    $('input[name="vehicle_me"]:checked').each(function(i){
        vel_me[i] = $(this).val();
    });
    console.log('vel_me: ' + vel_me);
    validation();
});

// Click on vehicle_them
var vel_them = [];
$('input[name="vehicle_them"]').click(function(){
    vel_them = [];
    $('input[name="vehicle_them"]:checked').each(function(i){
        vel_them[i] = $(this).val();
    });
    console.log('vel_them: ' + vel_them);
    validation();
});

// Click on court
var court = '';
$('input[name="court"]').click(function(){
    $('input[name="court"]:checked').each(function(){
        court = $(this).val();
        console.log('court: ' + court);
        validation();
    });
});

// Click on judge_situation
var judge_situation = [];
$('input[name="judge_situation"]').click(function(){
    judge_situation = [];
    $('input[name="judge_situation"]:checked').each(function(i){
        judge_situation[i] = $(this).val();
    });
    console.log('judge_situation: ' + judge_situation);
    validation();
});

// Click on crash_type
var crash_type = '';
$('input[name="crash_type"]').click(function(){
    $('input[name="crash_type"]:checked').each(function(){
        crash_type = $(this).val();
        console.log('crash_type: ' + crash_type);
        validation();
    });
});

// Click on daypart
var daypart = '';
$('input[name="daypart"]').click(function(){
    $('input[name="daypart"]:checked').each(function(){
        daypart = $(this).val();
        console.log('daypart: ' + daypart);
        validation();
    });
});

// Click on weather
var weather = [];
$('input[name="weather"]').click(function(){
    weather = [];
    $('input[name="weather"]:checked').each(function(i){
        weather[i] = $(this).val();
    });
    console.log('weather: ' + weather);
    validation();
});

// Click on road_type
var road_type = '';
$('input[name="road_type"]').click(function(){
    $('input[name="road_type"]:checked').each(function(){
        road_type = $(this).val();
        console.log('road_type: ' + road_type);
        validation();
    });
});

// Click on injured_condition
var injured_condition = '';
$('input[name="injured_condition"]').click(function(){
    $('input[name="injured_condition"]:checked').each(function(){
        injured_condition = $(this).val();
        console.log('injured_condition: ' + injured_condition);
        validation();
    });
});

// AJAX for show_summary
$('#show_verdicts_list').on('click', 'tr td', function(event){
    event.preventDefault();
    console.log("Show Summary!" + $(this).attr('name'));  // sanity check
    show_summary($(this).attr('name'));
});

function show_result() {
    $('#mychart, #verdicts').removeClass('resultsection');
};

function show_summary(num) {
    console.log("show summary is working!"+num); // sanity check
    $.ajax({
        url : "show_summary/"+num, // the endpoint
        type : "GET", // http method
        // data : { Judg_num : num }, // data sent with the post request

        // handle a successful response
        success : function(json){
            console.log(json['Verdict'].length); // log the returned json to the console
            console.log("success"); // another sanity check
            var items = [];
            for (i in json['Item']){items.push(json['Item'][i].item)};
            var lawyerP = [];
            for (i in json['LawyerP']){lawyerP.push(json['LawyerP'][i].lawyer)};
            lawyerP = ((lawyerP.length == 0) ? ['無'] : lawyerP);
            var lawyerD = [];
            for (i in json['LawyerD']){lawyerD.push(json['LawyerD'][i].lawyer)};
            lawyerD = ((lawyerD.length == 0) ? ['無'] : lawyerD);
            $("#show_summary").html("\
                                <li>案由: "+json['Verdict'][0].judgereason+"</li>\
                                <li>原告勝敗訴: "+json['Verdict'][0].judgeresult+"</li>\
                                <li>裁判日期: "+json['Verdict'][0].judg_date+"</li>\
                                <li>事故日期: "+json['Verdict'][0].acc_date+"</li>\
                                <li>歷時: </li>\
                                <li>判賠金額: "+json['Verdict'][0].total_damage+"</li>\
                                <li>求償項目: "+items+"</li>\
                                <li>是否有鑑定文件: "+json['Verdict'][0].inverstigation+"</li>\
                                <li>法官: "+json['Verdict'][0].judge+"法官"+"</li>\
                                <br>\
                                <li>原告訴訟費用: "+json['Verdict'][0].pfee+"</li>\
                                <li>原告主張: "+json['Verdict'][0].p_assertion+"</li>\
                                <li>原告律師: "+lawyerP+"</li>\
                                <br>\
                                <li>被告訴訟費用: "+json['Verdict'][0].dfee+"</li>\
                                <li>被告主張: "+json['Verdict'][0].d_assertion+"</li>\
                                <li>被告律師: "+lawyerD+"</li>\
                                <li><a href='/verdict/"+num+"' target='_blank' name='full_content'>完整判決"+num+"</a></li>")
        }
    });
};
// end of show_summary

// AJAX for searching
function search_verdict() {
    reset();
    console.log("search verdict is working!"); // sanity check
    $.ajax({
        url : "/search_verdict/", // the endpoint
        type : "GET", // http method
        data : { judgefee : $('#search-form input[name="judgefee"]:checked').val(),
                 p_d : p_d,
                 vel_me : vel_me.join(),
                 vel_them : vel_them.join(),
                 court : court,
                 judge_situation : judge_situation.join(),
                 crash_type : crash_type,
                 daypart : daypart,
                 weather : weather.join(),
                 road_type : road_type,
                 injured_condition : injured_condition,
                 }, // data sent with the post request

        // handle a successful response
        success : function(json){
            console.log(json['Attribute'].length); // log the returned json to the console
            $("#show_verdicts_list").html("");
            for (var i = json['Attribute'].length - 1; i >= json['Attribute'].length - 100; i--) {
                // json['Attribute'][i]
                $('#result_num').html("共 "+json['Attribute'].length+1+" 筆判決");
                $("#show_verdicts_list").prepend("<tr><td name="+json['Attribute'][i].judg_num+">"+json['Attribute'][i].judgeid+"</td></tr>");
                // $("#result").prepend("<li><a href='#' name="+json['Attribute'][i].judg_num+"><span>"+json['Attribute'][i].judgeid+"</span></a></li>");
                // $("#result").prepend("<li name="+json['Attribute'][i].judg_num+"><span>"+json['Attribute'][i].judgeid+"</span></li>");
                // $("#result").prepend("<li><strong>"+json['Attribute'][i].judgeid+"</strong> - <em> "+json['Attribute'][i].judgefee+"</em> - <span> "+json['Attribute'][i].total_damage+"</span></li>");
                // $("#result").prepend("<p>"+json['Attribute'][i].judgefee+"</p>")
                // console.log(json['Attribute'][i].judgeresult+', '+json['Attribute'][i].inverstigation+', '+json['Attribute'][i].d_assertion);

                // if (json['Attribute'][i].judgeresult == 'win') {win_lose['win']++;}
                // else {win_lose['lose']++;};

                // if (json['Attribute'][i].judgeresult == 'win' && json['Attribute'][i].inverstigation == 'True') {win_lose_doc['win']++;}
                // else{win_lose_doc['lose']++;};

                // if (json['Attribute'][i].judgeresult == 'win' && json['Attribute'][i].d_assertion == ' True') {win_lose_d['win']++;}
                // else{win_lose_d['lose']++;};

                if (json['Attribute'][i].judgeresult == 'win' && json['Attribute'][i].inverstigation == 'False' && json['Attribute'][i].p_assertion == 'False' && json['Attribute'][i].d_assertion == ' False')
                    { win_lose['ni_nl_nd'][0]++; } else { win_lose['ni_nl_nd'][1]++; };
                if (json['Attribute'][i].judgeresult == 'win' && json['Attribute'][i].inverstigation == 'True' && json['Attribute'][i].p_assertion == 'False' && json['Attribute'][i].d_assertion == ' False')
                    { win_lose['wi_nl_nd'][0]++; } else { win_lose['wi_nl_nd'][1]++; };
                if (json['Attribute'][i].judgeresult == 'win' && json['Attribute'][i].inverstigation == 'False' && json['Attribute'][i].p_assertion == 'True' && json['Attribute'][i].d_assertion == ' False')
                    { win_lose['ni_wl_nd'][0]++; } else { win_lose['ni_wl_nd'][1]++; };
                if (json['Attribute'][i].judgeresult == 'win' && json['Attribute'][i].inverstigation == 'False' && json['Attribute'][i].p_assertion == 'False' && json['Attribute'][i].d_assertion == ' True')
                    { win_lose['ni_nl_wd'][0]++; } else { win_lose['ni_nl_wd'][1]++; };
                if (json['Attribute'][i].judgeresult == 'win' && json['Attribute'][i].inverstigation == 'True' && json['Attribute'][i].p_assertion == 'True' && json['Attribute'][i].d_assertion == ' False')
                    { win_lose['wi_wl_nd'][0]++; } else { win_lose['wi_wl_nd'][1]++; };
                if (json['Attribute'][i].judgeresult == 'win' && json['Attribute'][i].inverstigation == 'True' && json['Attribute'][i].p_assertion == 'False' && json['Attribute'][i].d_assertion == ' True')
                    { win_lose['wi_nl_wd'][0]++; } else { win_lose['wi_nl_wd'][1]++; };
                if (json['Attribute'][i].judgeresult == 'win' && json['Attribute'][i].inverstigation == 'False' && json['Attribute'][i].p_assertion == 'True' && json['Attribute'][i].d_assertion == ' True')
                    { win_lose['ni_wl_wd'][0]++; } else { win_lose['ni_wl_wd'][1]++; };
                if (json['Attribute'][i].judgeresult == 'win' && json['Attribute'][i].inverstigation == 'True' && json['Attribute'][i].p_assertion == 'True' && json['Attribute'][i].d_assertion == ' True')
                    { win_lose['wi_wl_wd'][0]++; } else { win_lose['wi_wl_wd'][1]++; };


                if (json['Attribute'][i].judgeid.search('保') != -1) {
                    damagelist['保險'].push(json['Attribute'][i].total_damage);
                    daylist['保險'].push(json['Attribute'][i].judg_num);
                } else if (json['Attribute'][i].total_damage > 500000) {
                    damagelist['普通'].push(json['Attribute'][i].total_damage);
                    daylist['普通'].push(json['Attribute'][i].judg_num);
                } else if (json['Attribute'][i].total_damage < 100000) {
                    damagelist['小額'].push(json['Attribute'][i].total_damage);
                    daylist['小額'].push(json['Attribute'][i].judg_num);
                } else {
                    damagelist['簡易'].push(json['Attribute'][i].total_damage);
                    daylist['簡易'].push(json['Attribute'][i].judg_num);
                };

                console.log(json['Attribute'][i].p_assertion);
            };
            console.log(win_lose);
            show_summary(json['Attribute'][0].judg_num);
            
            for (var j in json['Ditems']) { damageitemcount[json['Ditems'][j].item]++; };
            chartitem = Object.keys(damageitemcount).map(function (key) {return [key, damageitemcount[key]]});
            
            // damagerange['普通'] = (damagelist['普通'].length != 0) ? [Math.min.apply(null,damagelist['普通']), Math.max.apply(null,damagelist['普通'])] : [];
            // damagerange['保險'] = (damagelist['保險'].length != 0) ? [Math.min.apply(null,damagelist['保險']), Math.max.apply(null,damagelist['保險'])] : [];
            // damagerange['小額'] = (damagelist['小額'].length != 0) ? [Math.min.apply(null,damagelist['小額']), Math.max.apply(null,damagelist['小額'])] : [];
            // damagerange['簡易'] = (damagelist['簡易'].length != 0) ? [Math.min.apply(null,damagelist['簡易']), Math.max.apply(null,damagelist['簡易'])] : [];

            for (var d in Object.keys(damagerange)) {
                var term = Object.keys(damagerange)[d];
                damagerange[term] = (damagelist[term].length != 0) ? [Math.min.apply(null,damagelist[term]), Math.max.apply(null,damagelist[term])] : [];
                dayrange[term] = (daylist[term].length != 0) ? [Math.min.apply(null,daylist[term]), Math.max.apply(null,daylist[term])] : [];
            };
            console.log("success"); // another sanity check

            // data prepared for chart
            // console.log('win: '+win_lose['win']);
            // console.log('lose: '+win_lose['lose']);
            // console.log('windoc: '+win_lose_doc['win']);
            // console.log('losedoc: '+win_lose_doc['lose']);
            // console.log('wind: '+win_lose_d['win']);
            // console.log('losed: '+win_lose_d['lose']);
            // console.log(damageitemcount);
            // console.log(chartitem);
            // console.log(damagelist);
            // console.log(damagerange['普通']);
            show_win_chart();
            show_item_chart();
            show_money_chart();
            show_day_chart();
            $('#ready h4').addClass('readytogo');
            $('#ready').removeClass('readyhide');

        }
        // // handle a non-successful response
        // error : function(xhr,errmsg,err) {
        //     $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
        //         " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        //     console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        // }
    });
};

// This function gets cookie with a given name
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

/*
The functions below will create a header with csrftoken
*/

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
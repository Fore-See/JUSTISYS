$(function() {

// nothing
console.log("nothing")

});

// Submit searxh on submit
$('#search-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});

// Click on p_d
var p_d = '';
$('input[name="p_d"]').click(function(){
    $('input[name="p_d"]:checked').each(function(){
        p_d = $(this).val();
        console.log('p_d: ' + p_d);
    });
});

// Click on vehicle_me
var vel_me = [];
$('input[name="vehicle_me"]').click(function(){
    vel_me = [];
    $('input[name="vehicle_me"]:checked').each(function(i){
        vel_me[i] = $(this).val();
    });
    console.log('vel_me: ' + vel_me);
});

// Click on vehicle_them
var vel_them = [];
$('input[name="vehicle_them"]').click(function(){
    vel_them = [];
    $('input[name="vehicle_them"]:checked').each(function(i){
        vel_them[i] = $(this).val();
    });
    console.log('vel_them: ' + vel_them);
});

// Click on court
var court = '';
$('input[name="court"]').click(function(){
    $('input[name="court"]:checked').each(function(){
        court = $(this).val();
        console.log('court: ' + court);
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
});

// Click on crash_type
var crash_type = '';
$('input[name="crash_type"]').click(function(){
    $('input[name="crash_type"]:checked').each(function(){
        crash_type = $(this).val();
        console.log('crash_type: ' + crash_type);
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
});

// Click on road_type
var road_type = '';
$('input[name="road_type"]').click(function(){
    $('input[name="road_type"]:checked').each(function(){
        road_type = $(this).val();
        console.log('road_type: ' + road_type);
    });
});

// Click on injured_condition
var injured_condition = '';
$('input[name="injured_condition"]').click(function(){
    $('input[name="injured_condition"]:checked').each(function(){
        injured_condition = $(this).val();
        console.log('injured_condition: ' + injured_condition);
    });
});

// AJAX for show_summary
$('#result').on('click', 'li a', function(event){
    event.preventDefault();
    console.log("Show Summary!" + $(this).attr('name'));  // sanity check
    show_summary($(this).attr('name'));
});

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
            $("#summary").html("<li>原告勝敗訴: "+json['Verdict'][0].judgeresult+"</li>\
                                <li>訴訟費用(雙方): "+json['Verdict'][0].judgefee+"</li>\
                                <li>判賠金額: "+json['Verdict'][0].total_damage+"</li>\
                                <li>是否有鑑定文件: "+json['Verdict'][0].inverstigation+"</li>\
                                <li>法官: "+json['Verdict'][0].judge+"</li>\
                                <a href='/verdict/"+num+"' target='_blank' name='full_content'>完整判決"+num+"<a>")
        }
    });
};
// end of show_summary

// AJAX for posting
function create_post() {
    console.log("create post is working!"); // sanity check
    $.ajax({
        url : "/create_post/", // the endpoint
        type : "POST", // http method
        data : { judgefee : $('#post-form input[name="judgefee"]:checked').val(),
                 p_d : p_d,
                 vel_me : vel_me.join(),
                 vel_them : vel_them.join(),
                 court : court,
                 judge_situation : judge_situation.join(),
                 crash_type : crash_type,
                 weather : weather.join(),
                 road_type : road_type,
                 injured_condition : injured_condition,
                 }, // data sent with the post request

        // handle a successful response
        success : function(json){
            console.log(json['Attribute'].length); // log the returned json to the console
            $("#result").html("");
            for (var i = json['Attribute'].length - 1; i >= json['Attribute'].length - 100; i--) {
                // json['Attribute'][i]
                $("#result").prepend("<li><a href='#' name="+json['Attribute'][i].judg_num+"><span>"+json['Attribute'][i].judgeid+"</span></a></li>");
                // $("#result").prepend("<li><a href='#' name="+json['Attribute'][i].judg_num+"><span>"+json['Attribute'][i].judgeid+"</span></a></li>");
                // $("#result").prepend("<li name="+json['Attribute'][i].judg_num+"><span>"+json['Attribute'][i].judgeid+"</span></li>");
                // $("#result").prepend("<li><strong>"+json['Attribute'][i].judgeid+"</strong> - <em> "+json['Attribute'][i].judgefee+"</em> - <span> "+json['Attribute'][i].total_damage+"</span></li>");
                // $("#result").prepend("<p>"+json['Attribute'][i].judgefee+"</p>")
            };
            console.log("success"); // another sanity check
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
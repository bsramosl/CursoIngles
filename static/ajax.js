var $ = jQuery.noConflict();

function submit_with_ajax(url, title, content, parameters, callback) {
    $.ajax({
        url: url, //window.location.pathname
        type: 'POST',
        data: parameters,
        dataType: 'json',
        processData: false,
        contentType: false,
    }).done(function (data) {
        console.log(data);
        if (!data.hasOwnProperty('error')) {
            callback();
            return false;
        }
        console.log(data.error); 
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ': ' + errorThrown);
    }).always(function (data) {

    });
}
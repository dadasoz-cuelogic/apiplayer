$(document).ready(function(){
    get_product_data();

    $("#oauth_dropdown").click(function(){
        $('.dropdown-menu-box').show();
    });

    $("#method_control").click(function(){
        console.log("test");
        $('#method_list_holder').show()
    });

});

$.postJSON = function(url, data, callback) {
    return jQuery.ajax({
        'type': 'POST',
        beforeSend: function (request)
            {
                request.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            },
        'url': url,
        'contentType': 'application/json',
        'data': JSON.stringify(data),
        'dataType': 'json',
        'success': callback
    });
};

function get_product_data(){
    post_data = {
        'product_name' : product,
    }
    $.postJSON('/api/get-data/',post_data,function(data,status){
        console.log(data);
        load_initial_data(data);
    });
}

function load_initial_data(data){
    $("#end_point").html("");
    endpoints = data.endpoints
    $.each(endpoints, function(index, endpoint) {
        end_point_html = '<option value="'+endpoint.base+'">'+endpoint.base+'</option>';
        $("#end_point").append(end_point_html);
        $.each(endpoint.resources, function(index, section) {
            console.log(section);
        });
    });
}
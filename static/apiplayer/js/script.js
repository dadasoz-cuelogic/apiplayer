$(document).ready(function(){
    get_product_data();

    $("#oauth_dropdown").click(function(){
        $('.dropdown-menu-box').show();
    });

    $("#method_control").click(function(){
        $('#method_list_holder').show();
        $("#method_toggle").addClass('method_toggle_rotate');
    });

    $("#request_tabs li").click(function(){
        $("#request_tabs li").removeClass('active');
        $(this).addClass("active");
        $("#request_params").find("table").hide();
        table = $(this).attr("data-pk");
        $("#request_params").find("#"+table).show();
    });

    $( "#token-model" ).dialog({
      autoOpen: false,
      width:400,
      height:280,
      modal:true,
    });

    $("#customtoken").click(function(){
        $( "#token-model" ).dialog("open");
        $('.dropdown-menu-box').hide();
    });

    $("#noauth").click(function(){
        $(".current_user").text("No Auth");
        $('.dropdown-menu-box').hide();
    });
    

    $(".save-token").click(function(){
        $('.dropdown-menu-box').hide();
        $( "#token-model" ).dialog("close");
        $(".current_user").text("Custom Token");
        $('form#authentication').addClass('submit_form');
    });

    $(".close-btn").click(function(){
        $( "#token-model" ).dialog("close");
    });
 

    $('#send_button').on('click', function() {
        var $inputs = $('.submit_form :input');
        var f = $inputs.serializeJSON();
        console.log(f);
        // not sure if you wanted this, but I thought I'd add it.
        // get an associative array of just the values.
        // var values = {};
        // $inputs.each(function() {
        //     values[this.name] = $(this).val();
        // });
        // console.log(values);
        return false;
    });


    $(document).on('click', '.add-post-query-header', function() {
        var tbody_id = $(this).closest('tbody').attr('id');
        tbody_id = $('#'+tbody_id);
        var len = tbody_id.find('tr').length;
        var $clone = tbody_id.find('tr:last').clone();
        $clone.find('td input').val('');
        $clone.find('td').each(function(i,v){
            for(var i = 1; i <= $(v).find('input').length; i++) {
                var name = $(v).find('input').attr('name').split('['+ parseInt(len - 1) +']')[1];
                $(v).find('input').eq(0).attr('name', '[req]['+len+']'+name);
            }
        });
        tbody_id.append($clone);
        html = '<td class="required_element" style="white-space: nowrap;"><button type="button" class="btn btn-sm btn-success pull-right remove-post-query-header">Remove</button></td>';
        if(len > 1 && len == 2) {
            tbody_id.find('tr:last td:last').after(html);
            tbody_id.find('tr:last td:last').remove();
        } else if(len <= 1) {
            tbody_id.find('tr:last td:last').remove();
            tbody_id.find('tr:last td:last').after(html);
        } 
    });

    $(document).on('click', '.remove-post-query-header', function() {
        $(this).closest('tr').remove();
    });

}); // End of document ready


var resourse_data = null;

var method_data = null;

$(document).on('click', '.click_parent', function() {
    method_id = parseInt($(this).attr('data-pk'));
    get_method(method_id);
    $('#method_list_holder').hide();
    setTimeout(function(){ 
        set_method(method_data);

    }, 500);
});

$(document).on('click', '.method_toggle_rotate', function() {
    $(this).removeClass('method_toggle_rotate');
    $('#method_list_holder').hide();
});

function set_method(data){
    method_name = data.method.name;
    display_name = data.method.display_name;
    method_id = data.method.id;
    path = data.path;
    params = data.method.params;
    $("#request_verb option").each(function() { this.selected = (this.text == method_name); });
    $("#request_bar_1").val(path);
    $("#request_tabs, #request_params").show();
    $('.tbody_req').html("")
    if(method_name==="GET"){
        $("#request_params").find("table").hide();
        $("#request_tabs li").removeClass('active');
        $("#query_tab").addClass("active");
        $("#request_params").find("#request_query").show();
        $.each(params, function(index, param) {
            required = "";
            required_class ="";
            required_bool ="False";
            if(param.required){
                required = '<sup class="sup_required">*</sup>';
                required_class ="";
                required_bool = "True";
            }
            html = '<tr class="js_tempField">';
            html += '<td>endpoints['+param.name+required+']</td>';
            html += '<td class="required_element" style="white-space: nowrap;"><input class="xlarge" placeholder="'+param.default+'" id="'+param.name+'" name="'+param.name+'" value="" required="'+required_bool+'" type="text"></td>';
            html += '<td>'+param.doc+'</td>';
            html += '</tr>';
            $("#request_params").find("#request_query_body").append(html);
        });
        html = '<tr class="js_tempField">';
        html += '<td class="required_element" style="white-space: nowrap;"><input class="xlarge" placeholder="Parameter" id="" name="endpoints[req][0][query-parameter]" value="" type="text"></td>';
        html += '<td class="required_element" style="white-space: nowrap;"><input class="xlarge" placeholder="Value" id="" name="endpoints[req][0][query-value]" value="" type="text"></td>';
        html += '<td class="required_element" style="white-space: nowrap;"><input class="xlarge" placeholder="Description" id="" name="endpoints[req][0][query-description]" value="" type="text"></td>';
        html += '<td class="required_element" style="white-space: nowrap;"><button type="button" class="btn btn-sm btn-success pull-right add-post-query-header">Add Row</button></td>';
        html += '</tr>';
        $("#request_params").find("#request_headers_body").append(html);

        html = '<tr class="js_tempField">';
        html += '<td class="required_element" style="white-space: nowrap;"><input class="xlarge" placeholder="Parameter" id="" name="endpoints[req][0][body-parameter]" value="" type="text"></td>';
        html += '<td class="required_element" style="white-space: nowrap;"><input class="xlarge" placeholder="Value" id="" name="endpoints[req][0][body-value]" value="" type="text"></td>';
        html += '<td class="required_element" style="white-space: nowrap;"><input class="xlarge" placeholder="Description" id="" name="endpoints[req][0][body-description]" value="" type="text"></td>';
        html += '<td class="required_element" style="white-space: nowrap;"><button type="button" class="btn btn-sm btn-success pull-right add-post-query-header">Add Row</button></td>';
        html += '</tr>';
        $("#request_params").find("#request_body").append(html);
    }
    else{
        $("#request_params").find("table").hide();
        $("#request_tabs li").removeClass('active');
        $("#body_tab").addClass("active");
        $("#request_params").find("#request_body").show();
        $.each(params, function(index, param) {
            required = "";
            required_class ="";
            required_bool ="False";
            if(param.required){
                required = '<sup class="sup_required">*</sup>';
                required_class ="";
                required_bool = "True";
            }
            html = '<tr class="js_tempField">';
            html += '<td>'+param.name+required+'</td>';
            html += '<td class="required_element" style="white-space: nowrap;"><input class="xlarge" placeholder="'+param.default+'" id="'+param.name+'" name="endpoints['+param.name+']" value="" required="'+required_bool+'" type="text"></td>';
            html += '<td>'+param.doc+'</td>';
            html += '</tr>';
            $("#request_params").find("#request_body_body").append(html);
        });
        html = '<tr class="js_tempField">';
        html += '<td class="required_element" style="white-space: nowrap;"><input class="xlarge" placeholder="Parameter" id="" name="endpoints[req][0][query-parameter]" value="" type="text"></td>';
        html += '<td class="required_element" style="white-space: nowrap;"><input class="xlarge" placeholder="Value" id="" name="endpoints[req][0][query-value]" value="" type="text"></td>';
        html += '<td class="required_element" style="white-space: nowrap;"><input class="xlarge" placeholder="Description" id="" name="endpoints[req][0][query-description]" value="" type="text"></td>';
        html += '<td class="required_element" style="white-space: nowrap;"><button type="button" class="btn btn-sm btn-success pull-right add-post-query-header">Add Row</button></td>';
        html += '</tr>';
        $("#request_params").find("#request_query_body").append(html);

        html = '<tr class="js_tempField">';
        html += '<td class="required_element" style="white-space: nowrap;"><input class="xlarge" placeholder="Parameter" id="" name="endpoints[req][0][header-parameter]" value="" type="text"></td>';
        html += '<td class="required_element" style="white-space: nowrap;"><input class="xlarge" placeholder="Value" id="" name="endpoints[req][0][header-value]" value="" type="text"></td>';
        html += '<td class="required_element" style="white-space: nowrap;"><input class="xlarge" placeholder="Description" id="" name="endpoints[req][0][header-description]" value="" type="text"></td>';
        html += '<td class="required_element" style="white-space: nowrap;"><button type="button" class="btn btn-sm btn-success pull-right add-post-query-header">Add Row</button></td>';
        html += '</tr>';
        $("#request_params").find("#request_headers_body").append(html);
    }

}

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
        load_initial_data(data);
        resourse_data = data;
    });
}

function load_initial_data(data){
    $("#end_point").html("");
    endpoints = data.endpoints
    $.each(endpoints, function(index, endpoint) {
        auth_required = 'auth_required';
        end_point_html = '<option value="'+endpoint.base+'">'+endpoint.base+'</option>';
        $("#end_point").append(end_point_html);
        $.each(endpoint.resources, function(index, section) {
            $.each(section, function(index, sub_section_all) {
                api_sections = '<section class="js_activeMethod js_methodSection base_0">';                                        
                $.each(sub_section_all, function(index, sub_section) {
                    if(index==0){
                        api_sections += '<strong>Create and Update Terms and Exams</strong><ul>';
                    }else{
                        method_name = sub_section.method.name;
                        method_id = sub_section.method.id;
                        display_name = sub_section.method.display_name;
                        b_color = '';
                        if(method_name==="GET"){
                           b_color = 'blue'; 
                        }else if(method_name==="POST"){
                           b_color = 'green'; 
                        }
                        else if(method_name==="PUT"){
                           b_color = 'brown'; 
                        }
                        else if(method_name==="DELETE"){
                           b_color = 'red'; 
                        }
                        auth_required = auth_required + ' ' + b_color;
                        api_sections += '<li class="click_parent js_methodMatch" data-pk='+method_id+' onclick="return false;" style="clear: both;"><span class="lozenge left '+auth_required+'">'+method_name+'</span><a class="provider_method click_child" title="'+display_name+'" href="javascript:void(0);">'+display_name+'</a></li>';
                    }
                    if(index == sub_section_all.lenght+1){
                        api_sections += '</ul></section>';
                    }
                });
                $("#resource_holder").html(api_sections);
            });
        });
    });
}


function get_method(id){
    endpoints = resourse_data.endpoints
    $.each(endpoints, function(index, endpoint) {
        $.each(endpoint.resources, function(index, section) {
            $.each(section, function(index, sub_section_all) {
                $.each(sub_section_all, function(index, sub_section) {
                    if(index != 0){
                        method_id = sub_section.method.id;
                        if(method_id === id){
                            method_data = sub_section;
                            return;
                        }
                    }
                });
            });
        });
    });
}
$(document).ready(function(){
	
	check_tr_row();
	check_auth_header_row();

	// For adding Body Params
	$('.add-row').on('click', function() {

		var tr = $('.req-body tbody').find('tr:last');
		var $clone = tr.clone();
		$clone.find('td div input').val('');
		$clone.find('td div input[type="checkbox"]').prop('checked', false);
		var counter = $('.req-tbody').find('tr').length;
        $clone.find('td').each(function(){
        	var $name = $(this).find('div input').attr('name').split('['+ parseInt(counter - 1) +']')[1];
            $(this).find('div input').eq(0).attr('name', 'endpoints[resources][auth][method][params]['+counter+']'+$name);
        });
        $(".req-body tbody").append($clone);
		check_tr_row();
	});

	// For adding Header Params
	$('.add-auth').on('click', function() {

		var tr = $('.auth-req-body tbody').find('tr:last');
		var $clone = tr.clone();
		$clone.find('td div input').val('');
		var counter = $('.auth-req-tbody').find('tr').length;
		$clone.find('td').each(function(){
            var $name = $(this).find('div input').attr('name').split('['+ parseInt(counter - 1) +']')[1];
            $(this).find('div input').eq(0).attr('name', 'endpoints[header]['+counter+']'+$name);
        });
		$(".auth-req-body tbody").append($clone);
		check_auth_header_row()
	});

	// For Removing body params
	$('.remove-row').live('click', function() {
		$(this).closest('tr').remove();
	});

	// For Removing header params
	$('.remove-auth-header-row').live('click', function() {
		$(this).closest('tr').remove();
	});


	$('form#endpoint').on('submit', function(e) {
		form_data = {
			'data' : $(this).serializeJSON(),
			'end_point' : $("#api-end-points option:selected").attr("data-pk"),
			'product_key' : $("#product-key").val(),
			'section' : $("#api-sections option:selected").attr("data-pk"),
		}

		$.post("/product/api/add/",form_data,function(data,status){
			if(data.message=="success"){
				alert("data saved!");
			}
		});
		return false;
	});


	$("#api-end-point-save").click(function(){
		post_data = {
			'end_point' : $("#api-end-point-input").val(),
			'product_key' : $("#product-key").val(),
		}
		
		$.post('/product/endpoint/add/',post_data,function(data,status){
			if(data.message=="success"){
				$("#api-end-point-input").val("");
				$("#modal-dialog").modal("hide");
				html = '<option value="'+data.end_point_name+'" data-pk="'+data.end_point_id+'">'+data.end_point_name+'</option>';
				$("#api-end-points").append(html);
			}
		});
	});

	$("#api-section-save").click(function(){
		post_data = {
			'end_point' : $("#api-end-points option:selected").attr("data-pk"),
			'product_key' : $("#product-key").val(),
			'section': $("#api-section-input").val(),
		}
		
		$.post('/product/section/add/',post_data,function(data,status){
			if(data.message=="success"){
				$("#api-section-input").val("");
				$("#modal-section").modal("hide");
				html = '<option value="'+data.section_name+'" data-pk="'+data.section_id+'">'+data.section_name+'</option>';
				$("#api-sections").append(html);
			}
		});
	});

	$("#view-player").click(function(data,status){
		$("#model-player-div").modal("show");
		url = "/api/player/"+$("#product-key").val()+'/';
		$("#frame-player").attr("src",url);
	});

}); //End of document ready


function check_tr_row() {
	len = $('.req-body tbody tr').length;
	var html = '<td><div class="col-md-12"><button type="button" class="btn btn-sm btn-success pull-right remove-row">X</button></div></td>';
	if(len > 1 && len == 2) {
		$('.req-body tbody tr td:last').after(html);
	} else if(len <= 1) {
		$('.req-body tbody tr td:last').remove();
	}
}


function check_auth_header_row() {
	len = $('.auth-req-body tbody tr').length;
	var html = '<td><div class="col-md-12"><button type="button" class="btn btn-sm btn-success pull-right remove-auth-header-row">X</button></div></td>';
	if(len > 1 && len == 2) {
		$('.auth-req-body tbody tr td:last').after(html);
	} else if(len <= 1) {
		$('.auth-req-body tbody tr td:last').remove();
	}
}
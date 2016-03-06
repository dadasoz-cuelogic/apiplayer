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
        	for(var i = 1; i <= $(this).find('div input').length; i++) {
        		var $name = $(this).find('div input').attr('name').split('['+ parseInt(counter - 1) +']')[1];
            	$(this).find('div input').eq(0).attr('name', 'endpoints[resources][auth][method][params]['+counter+']'+$name);
        	}
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
			for(var i = 1; i <= $(this).find('div input').length; i++) {
				var $name = $(this).find('div input').attr('name').split('['+ parseInt(counter - 1) +']')[1];
            	$(this).find('div input').eq(0).attr('name', 'endpoints[header]['+counter+']'+$name);
			}
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
		console.log($(this).serializeJSON());
		return false;
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
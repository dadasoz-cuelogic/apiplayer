$(document).ready(function(){

	$(document).on("click", '.save-product', function(){
        data = {
            productName : $("#product-name").val(),
            productUrl : $("#product-url").val(),
            productEndPoint : $("#product-endpoint").val(),
            productSection : $("#product-section").val(),
            productCategory: $("#product-category").val(),
            apiStatus : $('input[name=is_active]:checked').val(),
            csrfmiddlewaretoken : $('#csrfmiddlewaretoken').val()
        }

        $.post("/product/add-product/", data, function(data,status){
            $.showNotification("Success", "product added");
        });
    });
});

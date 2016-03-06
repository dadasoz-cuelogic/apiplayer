$(document).ready(function(){

	$(document).on("click", '.save-product', function(){
        data = {
            productName : $("#product-name").val(),
            productUrl : $("#product-url").val(),
            productEndPoint : $("#product-endpoint").val(),
            productCategory: $("#product-category").val(),
            apiStatus : $('input[name=is_active]:checked').val(),
            api_visibility : $('input[name=visibility]:checked').val(),
            csrfmiddlewaretoken : $('#csrfmiddlewaretoken').val()
        }
        $.post("/product/add/", data, function(data,status){
            if(data.message=="success"){
                document.location ="/product/edit/"+data.product_key+'/';
            }else{
                alert("error");
            }
        });
    });
});

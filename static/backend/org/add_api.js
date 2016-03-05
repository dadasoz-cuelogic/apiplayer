$(document).ready(function(){
	fetch_categories()
});



function fetch_categories() {
    $.get("/product/get-all-categories/", {}, function(data, status) {
        console.log(data);
    });
}
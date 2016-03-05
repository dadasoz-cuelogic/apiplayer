// Global decalarations


// Document ready
$(document).ready(function() {
	get_all_categories();
	get_all_products_in_category();
});

// Get all categories
function get_all_categories() {
    $.get("/dev/categories", {}, function(data, status) {
    });
}

// Get products of selected category

function get_all_products_in_category() {
    $.get("/dev/products-category", {'category': "null"}, function(data, status) {
    });
}
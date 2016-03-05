// Global decalarations


// Document ready
$(document).ready(function() {
    get_all_categories();
    get_all_products();
});

// Get all categories
function get_all_categories() {
    $.get("/dev/categories/", {}, function(categories_list, status) {
        if (status == "success") {
            categoryListObj = $(".category-list");
            $.each(categories_list, function(index, category) {
                categoryName = category.category_name;
                html = "";
                html += '<li class="category" data-text="'+categoryName+'" data-value="'+categoryName+'"><a href="#">'+categoryName+'</a></li>';
                categoryListObj.append(html);
            });
        }
    });
}

// On category selection
$(document).on('click', '.category', function() {
    var category_name = $(this).attr("data-value");
    get_all_products_in_category(category_name);
});

// Get products of selected category

function get_all_products_in_category(category_name) {
    $.get("/dev/products-category/", {'category': category_name}, function(data, status) {
        console.log("This is get_all_products_in_category");
    });
}

// Get all products
function get_all_products() {
    $.get("/dev/all-products-category/",{}, function(product_list, status) {
        console.log("This is get_all_products");
        render_product_gallery(product_list);
    });
}

function render_product_gallery(product_list) {
        $.each(product_list, function(index, product) {
        });
    }
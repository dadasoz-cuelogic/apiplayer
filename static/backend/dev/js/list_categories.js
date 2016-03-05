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
    $.get("/dev/products-category/", {'category': category_name}, function(product_list, status) {
        render_product_gallery(product_list);
    });
}

// Get all products
function get_all_products() {
    $.get("/dev/all-products-category/",{}, function(product_list, status) {
        render_product_gallery(product_list);
    });
}

function render_product_gallery(product_list) {
    $('.gallery').html("");

    if (product_list.length > 0) {
        $.each(product_list, function(index, product) {
            html = '';
            html += '<div class="image gallery-group-1 col-md-3">';
            html += '<div class="image-inner">';
            html += '<a href="'+product.product_api_player_url+'" data-lightbox="gallery-group-1">';
            html += '<img src="/static/backend/assets/img/gallery/gallery-1.jpg" alt="" />';
            html += '</a>';
            html += '<p class="image-caption">';
            html += product.product_category;
            html += '</p>';
            html += '</div>';
            html += '<div class="image-info">';
            html += '<h5 class="title">'+product.product_name+'</h5>';
            html += '<div class="pull-right">';
            html += '<small>from </small> <a href="javascript:;">'+product.product_organization+'</a>';
            html += '</div>';
            html += '<div class="rating">';
            html += '<span class="star active"></span>';
            html += '<span class="star active"></span>';
            html += '<span class="star active"></span>';
            html += '<span class="star"></span>';
            html += '<span class="star"></span>';
            html += '</div>';
            html += '<div class="desc">';
            html +=  product.product_description;
            html += '</div>';
            html += '</div>';
            html += '</div>';
            $('.gallery').append(html);
        });
    } else {
        $('.gallery').append("<h2 class='no-record-found'>No Products Found....</h2>");
    }
}


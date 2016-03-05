"""
Logic for dev.

Implementation of dev views.
"""
# from django.shortcuts import render
import json

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from product.models import Catagory, Product
from django.template import RequestContext


def dashboard(request):
    """
    Display the all categorires apis.

    Render dashboard template.
    """
    return render_to_response('backend/dev/dashboard.html', {}, context_instance=RequestContext(request))


@require_GET
def get_all_categories(request):
    """
    Return all categories in JSON.

    Fetch from db
    """
    categories_list = []

    try:
        categories_list = Catagory.objects.filter(is_active=True, is_deleted=False)
    except ObjectDoesNotExist:
        return HttpResponse(
            json.dumps({"Error": "object id not available"}),
            content_type='application/json'
        )
    category_response = []
    for category in categories_list:
        category_dict = {
            'category_name': category.name,
        }
        category_response.append(category_dict)

    return HttpResponse(json.dumps(category_response),
                        content_type='application/json')


@require_GET
def get_all_products_in_category(request):
    """
    Return products's of a particualr Category.

    Fetch from db
    """
    product_list = []
    catagory_name = request.GET.get('category', None)
    try:
        product_list = Product.objects.filter(is_active=True, is_deleted=False, catagory__name=catagory_name)
    except ObjectDoesNotExist:
        return HttpResponse(
            json.dumps({"Error": "object id not available"}),
            content_type='application/json'
        )

    product_response = []

    for product in product_list:
        product_dict = {
            'product_name': product.name,
            'product_url': product.url,
            'product_description': product.description,
            'product_category': product.catagory.name,
            'product_organization': product.organization.org_name
        }
        product_response.append(product_dict)

    return HttpResponse(json.dumps(product_response),
                        content_type='application/json')


@require_GET
def get_all_products(request):
    """
    Return all products.

    Fetch from db
    """
    product_list = []

    try:
        product_list = Product.objects.filter(is_active=True, is_deleted=False)
    except ObjectDoesNotExist:
        return HttpResponse(
            json.dumps({"Error": "object id not available"}),
            content_type='application/json'
        )

    product_response = []

    for product in product_list:
        product_dict = {
            'product_name': product.name,
            'product_url': product.url,
            'product_description': product.description,
            'product_category': product.catagory.name,
            'product_organization': product.organization.org_name
        }
        product_response.append(product_dict)

    return HttpResponse(json.dumps(product_response),
                        content_type='application/json')

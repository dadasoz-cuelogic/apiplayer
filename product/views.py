import json
import uuid
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
# from django.core.serializers import serialize
from django.http import HttpResponse
from product.models import Catagory, Product
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from organization.models import Organization
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/")
def get_all_categories(request):
    categories = Catagory.objects.filter(is_active=True)
    category_list = []
    for category in categories:
        category_list.append(
            form_category_dictionary(category))

    return HttpResponse(json.dumps(category_list),
                        content_type='application/json')

@login_required(login_url="/")
def form_category_dictionary(category):
    category_dict = {}
    category_dict['category_id'] = category.id
    category_dict['name'] = category.name
    return category_dict


@csrf_exempt
@login_required(login_url="/")
def add_product(request):
    if request.method == "POST":

        product_data = request.POST

        product_key = uuid.uuid4().hex

        product = Product(name=product_data.get("productName",""),
                          url=product_data.get("productUrl",""),
                          is_active=True,
                          description=product_data.get("description", ""),
                          product_type=product_data.get("productType", 1),
                          catagory=Catagory.objects.get(pk=int(product_data.get("productCategory"))),
                          organization=Organization.objects.get(pk=1),
                          product_key=product_key)
        try:
            product.save()
            return HttpResponse(json.dumps({"message": 'success'}), content_type="application/json")
        except:
            return HttpResponse(json.dumps({"message": 'error'}), content_type="application/json")
    categories = Catagory.objects.filter(is_active=True)
    return render_to_response("backend/org/add_product.html", {'categories': categories}, context_instance=RequestContext(request))


@csrf_exempt
@login_required(login_url="/")
def view_product(request):
    org = Organization.objects.filter(user=request.user)
    products = Product.objects.filter(organization=org)
    return render_to_response("backend/org/view_products.html", {'products': products}, context_instance=RequestContext(request))


@login_required(login_url="/")
def dashboard_iframe(request, product_key):
    """
    Display the all categorires apis.

    Render dashboard template.
    """
    return render_to_response('backend/org/dashboard_iframe.html', {product_key: product_key})


@login_required(login_url="/")
def edit_product(request,product_key):
      product = Product.objects.get(product_key=product_key)
      return render_to_response('backend/org/edit_product.html', {'product': product})

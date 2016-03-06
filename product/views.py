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
from api.models import EndPoint, Section, Apis

# Create your views here.


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

        product = Product(name=product_data.get("productName", ""),
                          url=product_data.get("productUrl", ""),
                          is_active=True,
                          description=product_data.get("description", ""),
                          product_type=product_data.get("productType", 1),
                          catagory=Catagory.objects.get(
                              pk=int(product_data.get("productCategory"))),
                          organization=Organization.objects.get(pk=1),
                          product_key=product_key)
        try:
            product.save()
            return HttpResponse(json.dumps({"message": 'success', 'product_key': product.product_key}), content_type="application/json")
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


@csrf_exempt
def edit_product(request, product_key):
    product = Product.objects.get(product_key=product_key)
    endpoints = EndPoint.objects.filter(product=product)
    sections = None
    if len(endpoints) > 0:
        sections = Section.objects.filter(endpoint=endpoints[0])
    return render(request, "backend/org/edit_product.html", {'product': product, 'endpoints': endpoints, 'sections': sections}, context_instance=RequestContext(request))


@csrf_exempt
def add_endpoint(request):
    if request.method == "POST":
        request_data = request.POST
        end_point = request_data.get("end_point", "")
        product_key = request_data.get("product_key", "")

        product = Product.objects.get(product_key=product_key)

        endpoint = EndPoint(name=end_point, description="", product=product)

        endpoint.save()

    return HttpResponse(json.dumps({"message": 'success', 'end_point_name': end_point, 'end_point_id': endpoint.id}), content_type="application/json")


@csrf_exempt
def add_section(request):
    if request.method == "POST":
        request_data = request.POST
        end_point = request_data.get("end_point", "")
        section_name = request_data.get("section", "")

        endpoint = EndPoint.objects.get(id=end_point)

        section = Section(name=section_name, endpoint=endpoint)

        section.save()

    return HttpResponse(json.dumps({"message": 'success', 'section_name': section.name, 'section_id': section.id}), content_type="application/json")


def getFilterdData(data):
    ds = json.loads(data)
    return ds.get('endpoints').get('resources')


@csrf_exempt
def add_api(request):
    if request.method == "POST":
        request_data = request.POST
        end_point = request_data.get("end_point", "")
        product_key = request_data.get("product_key", "")
        section_id = request_data.get("section", "")

        data = getFilterdData(request_data.get("data", ""))

        product = Product.objects.get(product_key=product_key)

        endpoint = EndPoint.objects.get(id=end_point)

        section = Section.objects.get(id=section_id)

        apis = Apis(data=data, section=section)

        apis.save()

        data['auth'].update({'id': apis.id, 'section': section.name})

        apis.data = data

        apis.save()

    return HttpResponse(json.dumps({"message": 'success'}), content_type="application/json")


@login_required(login_url="/")
def dashboard_iframe(request, product_key):
    """
    Display the all categorires apis.

    Render dashboard template.
    """
    return render_to_response('backend/org/dashboard_iframe.html', {product_key: product_key})


@login_required(login_url="/")
def edit_product(request, product_key):
    product = Product.objects.get(product_key=product_key)
    return render_to_response('backend/org/edit_product.html', {'product': product})

import json
import uuid
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
# from django.core.serializers import serialize
from django.http import HttpResponse
from product.models import Catagory, Product
from django.views.decorators.csrf import csrf_exempt
from organization.models import Organization

# Create your views here.

def get_all_categories(request):
    categories = Catagory.objects.filter(is_active=True)
    category_list = []
    for category in categories:
        category_list.append(
            form_category_dictionary(category))

    return HttpResponse(json.dumps(category_list),
                        content_type='application/json')


def form_category_dictionary(category):
    category_dict = {}
    category_dict['category_id'] = category.id
    category_dict['name'] = category.name
    return category_dict

@csrf_exempt
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
            # import pdb
            # pdb.set_trace()
            product.save()
            return HttpResponse(json.dumps({"message":'success'}), content_type="application/json")
        except:
            return HttpResponse(json.dumps({"message":'error'}), content_type="application/json")
    categories =  Catagory.objects.filter(is_active=True)
    return render_to_response("backend/org/add_api.html", {'categories': categories})

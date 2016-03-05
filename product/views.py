import json
from django.shortcuts import render
# from django.core.serializers import serialize
from django.http import HttpResponse
from product.models import Catagory


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

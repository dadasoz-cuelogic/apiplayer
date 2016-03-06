from django.shortcuts import render_to_response, render
from django.http import HttpResponse
import json
from product.models import Product
from django.template import RequestContext
from api.models import EndPoint, Section, Apis
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


from django.contrib.auth.decorators import login_required

# Create your views here.

@csrf_exempt
def player(request, product_key):
    data_dict = {}
    product = Product.objects.get(product_key=product_key)
    endpoints = EndPoint.objects.filter(product=product)
    return render(request, 'player/player.html', {'product': product, 'endpoints': endpoints})


@csrf_exempt
def get_data(request):
    if request.method == "POST":
        end_point = request.POST.get('end_point')
        data_dict = {}
        endpoint = EndPoint.objects.get(name=end_point)
        data_dict.update({'endpoints': [{'base': endpoint.name}]})
        sections = Section.objects.filter(endpoint=endpoint)
        resources = []
        for section in sections:
            apis = Apis.objects.filter(section=section)
            for api in apis:
                resources.append(api.data.itervalues().next())
        data_dict['endpoints'][0].update({'resources': resources})

        return HttpResponse(json.dumps(data_dict),
                            content_type='application/json')


@csrf_exempt
def post_api(request):
    data_dict = {}
    if request.method == "POST":
        data_dict = request.POST
    return HttpResponse(json.dumps(data_dict),
                        content_type='application/json')

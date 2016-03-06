from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
from product.models import Product
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/")
def player(request, product_key):
    product = Product.objects.get(pk=1)
    return render_to_response('player/player.html', {'product': product})


@login_required(login_url="/")
def get_data(request):
    data = {
        'endpoints': [{
            'base': 'https://x.proctoru.com/api/',
            'request_headers': [{
                    'token': '000025225hdhs'
            }],
            'resources': [{
                'Auth': [{
                    'section': 'Login and Authentication',
                },

                    {
                    'path': 'getInfo',
                    'method': {
                            'id': 1,
                            'name': 'GET',
                            'display_name': 'Get user info',
                            'params': [{
                                "name": "time_sent",
                                "required": True,
                                "type": "dateTime",
                                "doc": "",
                                "default": '',
                            }]
                    }
                },
                    {
                    'path': 'Login',
                        'method': {
                            'id': 2,
                            'name': 'POST',
                            'display_name': 'Login using this',
                            'params': [{
                                "name": "username",
                                "required": True,
                                "type": "varchar",
                                "doc": "",
                                "default": '',
                            },
                                {
                                "name": "password",
                                "required": True,
                                "type": "password",
                                "doc": "",
                                "default": '',
                            }]
                        }
                }],
            }]
        }]
    }

    return HttpResponse(json.dumps(data),
                        content_type='application/json')

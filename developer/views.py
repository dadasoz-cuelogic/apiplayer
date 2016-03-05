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


def dashboard(request):
    """
    Display the all categorires apis.

    Render dashboard template.
    """
    return render_to_response('backend/dev/dashboard.html', {})


def get_all_categories(request):
    """
    Return all categories in JSON.

    Fetch from db
    """
    categories_list = {}
    return HttpResponse(json.dumps(categories_list),
                        content_type='application/json')


def get_all_products_in_category(request):
    """
    Return products's of a particualr Category.

    Fetch from db
    """
    product_list = {}
    return HttpResponse(json.dumps(product_list),
                        content_type='application/json')

# Imports Error, and render as response
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from api.models import EndPoint
from product.models import Catagory
from organization.models import Organization
from django.template import RequestContext


def dashboard(request):
    return render_to_response('backend/org/dashboard.html', {})


def add_api(request):
    if request.method == "POST":
        name = request.POST.get
        return HttpResponse("hello")
    categories =  Catagory.objects.filter(is_active=True)
    return render_to_response("backend/org/add_api.html", {'categories': categories}, context_instance=RequestContext(request))


def endpoint(request):
    if request.method == "POST":
        name = request.POST.get('endpoint-name')
        return HttpResponse(name)
    return render(request, "backend/org/endpoint.html", {}, context_instance=RequestContext(request))


def create_request(request):
    if request.method == "POST":
        name = request.POST
        return HttpResponse(name)
    return render(request, "backend/org/create_request.html", {}, context_instance=RequestContext(request))

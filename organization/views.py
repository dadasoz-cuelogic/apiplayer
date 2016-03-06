# Imports Error, and render as response
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from api.models import EndPoint
from product.models import Catagory
from organization.models import Organization
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


@login_required(login_url="/")
def dashboard(request):
    return render(request,'backend/org/dashboard.html', {})


@login_required(login_url="/")
def add_api(request):
    if request.method == "POST":
        name = request.POST.get
        return HttpResponse("hello")
    categories = Catagory.objects.filter(is_active=True)
    return render(request,"backend/org/add_api.html", {'categories': categories})


@login_required(login_url="/")
def endpoint(request):
    if request.method == "POST":
        name = request.POST.get('endpoint-name')
        return HttpResponse(name)
    return render(request, "backend/org/endpoint.html", {})


@login_required(login_url="/")
def create_request(request):
    if request.method == "POST":
        name = request.POST
        return HttpResponse(name)
    return render(request, "backend/org/create_request.html", {})

# Imports Error, and render as response
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from api.models import EndPoint


def dashboard(request):
    return render_to_response('backend/org/dashboard.html', {})


def add_api(request):
    if request.method == "POST":
        name = request.POST.get
        return HttpResponse("hello")
    return render_to_response("backend/org/add_api.html", {})


def endpoint(request):
    if request.method == "POST":
        name = request.POST.get('endpoint-name')
        return HttpResponse(name)
    return render(request, "backend/org/endpoint.html", {})


def create_request(request):
    if request.method == "POST":
        name = request.POST
        return HttpResponse(name)
    return render(request, "backend/org/create_request.html", {})

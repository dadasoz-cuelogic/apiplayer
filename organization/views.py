# Imports Error, and render as response
from django.shortcuts import render_to_response
from django.http import HttpResponse


def dashboard(request):
    return render_to_response('backend/org/dashboard.html', {})


def add_api(request):
    if request.method == "POST":
        print request.POST
        return HttpResponse("hello")
    return render_to_response("backend/org/add_api.html", {})

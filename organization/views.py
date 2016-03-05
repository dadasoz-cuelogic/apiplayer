# Imports Error, and render as response
from django.shortcuts import render_to_response


def dashboard(request):
    return render_to_response('backend/org/dashboard.html', {})

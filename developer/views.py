# from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def dashboard(request):
    return render_to_response('backend/dev/dashboard.html', {})
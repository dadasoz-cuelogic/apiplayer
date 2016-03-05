# Imports Error, and render as response
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

def index(request):
    return render_to_response('frontend/index.html', {}, context_instance=RequestContext(request))

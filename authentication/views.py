import json
from django.shortcuts import render, render_to_response
from api_user.models import API_USER
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
# Create your views here.


@csrf_exempt
def login_view(request):

    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            api_user = API_USER.objects.get(user=user)
            if api_user.user_type == 1:
                return HttpResponse(json.dumps({'message': "success", 'user': "admin"}),
                                    content_type="application/json")
            if api_user.user_type == 3:
                return HttpResponse(json.dumps({'message': "success", 'user': "dev"}),
                                    content_type="application/json")
            if api_user.user_type == 2:
                return HttpResponse(json.dumps({'message': "success", 'user': "org"}),
                                    content_type="application/json")
    return HttpResponse(json.dumps({'message': "error"}),
                        content_type="application/json")


def logout_view(request):
    logout(request)
    return render_to_response('frontend/index.html', {}, context_instance=RequestContext(request))

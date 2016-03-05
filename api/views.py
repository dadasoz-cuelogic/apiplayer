from django.shortcuts import render_to_response

# Create your views here.

def player(request):
    return render_to_response('player/player.html', {})
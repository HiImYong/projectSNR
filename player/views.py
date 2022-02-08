from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from player.models import Player


def playerMain(request: HttpRequest):
    getPlayers = Player.objects.all().order_by('name')
    return render(request, "player/playerMain.html", {'playerItems': getPlayers, })

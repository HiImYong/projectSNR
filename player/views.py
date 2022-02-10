from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from player.models import Player


def playerMain(request: HttpRequest):
    getPlayers = Player.objects.all().order_by('name')
    return render(request, "player/playerMain.html", {'playerItems': getPlayers, })


def playerDetail(request, parameter):
    getPlayerQs = Player.objects.filter(id=parameter)
    getPlayer = getPlayerQs.first()
    return render(request, "player/playerDetail.html", {'playerItems': getPlayer, })


def likePlayer(request, parameter, self=None):
    getPlayerQs = Player.objects.filter(id=parameter) # 딕셔너리 변수에 파라미터를 받아와 라켓들 넣어줌
    getPlayer = getPlayerQs.first() # 혹시 모르니까 첫번째 라켓만 딕셔너리에서 빼냄
    checkUser = getPlayer.like.filter(id=request.user.id)  # name이 와서는 안되나요? # 리퀘스트와 함께 온 라켓정보와 유저 정보 중 디비를 뒤져서 id를 통해 좋아요한 유저 빼냄.
    if checkUser.exists():  # 만약에 해당 라켓에 이전에 그 유저가 좋아요를 했다면
        getPlayer.like.remove(request.user)  # 해당 유저 정보를 삭제함. 이 때
    else:
        getPlayer.like.add(request.user)
        getLikeCount = getPlayer.like.all().aggregate(Count('id'))['id__count']
        print(getLikeCount)
        getPlayer.countLike = getLikeCount
        getPlayer.save(self)

    return redirect('player:playerDetail', parameter=parameter)

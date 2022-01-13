from django.http import HttpRequest
from django.shortcuts import render

from racket.models import Racket


def racketMain(request: HttpRequest):
    getSearchKeyword = request.GET.get('searchKeyword','')

    if getSearchKeyword:
        getRacketList = Racket.objects.filter(name__icontains=getSearchKeyword).order_by('name')

    else:
        getRacketList = Racket.objects.order_by('id')

    return render(request, "racket/racketMain.html", {'racketList': getRacketList})


def racketDetail(request, parameter):
    getRacket = Racket.objects.get(id=parameter)
    return None
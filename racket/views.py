from django.http import HttpRequest
from django.shortcuts import render

from racket.models import Racket


def racketMain(request: HttpRequest):
    getRacketList = Racket.objects.order_by('id')
    return render(request, "racket/racketMain.html", {'racketList': getRacketList})

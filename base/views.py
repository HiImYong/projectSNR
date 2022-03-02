import requests
from django.db.models import Avg
from django.http import HttpRequest
from django.shortcuts import render

from racket.models import Racket
from racketReview.models import RacketReviewModel


def index(request: HttpRequest):
    getRacket = Racket.objects.order_by('name')
    getAvgScore = RacketReviewModel.objects.filter(visitorRacket_id=1).aggregate(Avg('visitorScore'))

    return render(request, "main.html", {'racketItems': getRacket,
                                         'racketUserScore': getAvgScore})


def aboutSNR(request: HttpRequest):
    r = requests.get('https://api.racketlogger.com/rackets')
    data = r.json()
    for ele in data:
        print(ele['brand'])
    return render(request, "about/aboutSNR.html", {})



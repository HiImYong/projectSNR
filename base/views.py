from django.db.models import Avg
from django.http import HttpRequest
from django.shortcuts import render

from racket.models import Racket
from visitor.models import VisitorReview


def index(request: HttpRequest):
    getRacket = Racket.objects.order_by('name')
    getAvgScore = VisitorReview.objects.filter(visitorRacket_id=1).aggregate(Avg('visitorScore'))

    return render(request, "main.html", {'racketItems': getRacket,
                                         'racketUserScore': getAvgScore})


def aboutSNR(request: HttpRequest):
    return render(request, "about/aboutSNR.html", {})

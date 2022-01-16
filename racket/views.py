from django.http import HttpRequest
from django.shortcuts import render

import visitor.forms
from racket.models import Racket, RacketDetail


def racketMain(request: HttpRequest):
    getSearchKeyword = request.GET.get('searchKeyword', '')

    if getSearchKeyword:
        getRacket = Racket.objects.filter(name__icontains=getSearchKeyword).order_by('name')

    else:
        getRacket = Racket.objects.order_by('id')

    return render(request, "racket/racketMain.html", {'racketItems': getRacket})


def racketDetail(request, parameter):
    getRacket = Racket.objects.filter(id=parameter)
    getRacketDetail = RacketDetail.objects.filter(racket_id=parameter)
    getReviewForm = visitor.forms.ReviewForm()

    return render(request, 'racket/racketDetail.html', {'racketItems': getRacket,
                                                        'racketDetailItems': getRacketDetail,
                                                        'racketReviewForm': getReviewForm})

from django.db.models import Avg, Func, FloatField, F
from django.http import HttpRequest
from django.shortcuts import render

import visitor.forms
from racket.models import Racket, RacketDetail
from visitor.models import VisitorReview


class Round(Func):
  function = 'ROUND'

def racketMain(request: HttpRequest):
    getSearchKeyword = request.GET.get('searchKeyword', '')

    if getSearchKeyword:
        getRacket = Racket.objects.filter(name__icontains=getSearchKeyword).order_by('name')

    else:
        getRacket = Racket.objects.order_by('id')

    # getRacket = VisitorReview.objects.filter
    # getRacketAvgScore =

    return render(request, "racket/racketMain.html", {'racketItems': getRacket})


def racketDetail(request, parameter):
    getRacketQs = Racket.objects.filter(id=parameter)
    getRacket = getRacketQs.first()
    getRacketDetail = RacketDetail.objects.filter(racket_id=parameter)
    getReviewForm = visitor.forms.ReviewForm()
    getReivewList = VisitorReview.objects.filter(visitorRacket_id=parameter)

    getAvgScore = VisitorReview.objects.filter(visitorRacket_id=parameter).aggregate(Avg('visitorScore'))
    # getAvgScore = VisitorReview.objects.filter(visitorRacket_id=parameter).aggregate(average_completion=Round(Avg(F('visitorScore')), 2), output_field=FloatField())

    return render(request, 'racket/racketDetail.html', {'racketItems': getRacket,
                                                        'racketDetailItems': getRacketDetail,
                                                        'racketReviewForm': getReviewForm,
                                                        'racketReivewListItems': getReivewList,
                                                        'racketAvgScoreItem': getAvgScore
                                                        })

from django.db.models import Avg, Func, FloatField, F
from django.http import HttpRequest
from django.shortcuts import render

import visitor.forms
from racket.models import Racket, RacketDetail
from visitor.models import VisitorReview





def racketMain(request: HttpRequest):

    getSearchKeyword = request.GET.get('searchKeyword', '')
    sort = request.GET.get('sort', '')


    if getSearchKeyword:
        getRacket = Racket.objects.filter(name__icontains=getSearchKeyword).order_by('name')
        getAdminScore = RacketDetail.objects.get(racket_id=1)
        getAvgScore = VisitorReview.objects.filter(visitorRacket_id=1).aggregate(Avg('visitorScore'))


    else:
        if sort == 'names':
            getRacket = Racket.objects.order_by('name')
            getAdminScore = RacketDetail.objects.get(racket_id=1)
            # getAdminScore = RacketDetail.objects.get(racket_id=getRacket.id)
            getAvgScore = VisitorReview.objects.filter(visitorRacket_id=1).aggregate(Avg('visitorScore'))
        elif sort == 'id' or '':
            getRacket = Racket.objects.order_by('id')
            getAdminScore = RacketDetail.objects.get(racket_id=1)
            # getAdminScore = RacketDetail.objects.get(racket_id=getRacket.id)
            getAvgScore = VisitorReview.objects.filter(visitorRacket_id=1).aggregate(Avg('visitorScore'))
        else:
            getRacket = Racket.objects.order_by('name')
            getAdminScore = RacketDetail.objects.get(racket_id=1)
            # getAdminScore = RacketDetail.objects.get(racket_id=getRacket.id)
            getAvgScore = VisitorReview.objects.filter(visitorRacket_id=1).aggregate(Avg('visitorScore'))




    # getRacket = VisitorReview.objects.filter
    # getRacketAvgScore =

    return render(request, "racket/racketMain.html", {'racketItems': getRacket,
                                                      'racketAdminScore': getAdminScore,
                                                      'racketUserScore': getAvgScore})


def racketDetail(request, parameter):
    getRacketQs = Racket.objects.filter(id=parameter)
    getRacket = getRacketQs.first()
    getRacketDetail = RacketDetail.objects.filter(racket_id=parameter)
    getReviewForm = visitor.forms.ReviewForm()
    getReivewList = VisitorReview.objects.filter(visitorRacket_id=parameter)

    getAvgScore = VisitorReview.objects.filter(visitorRacket_id=parameter).aggregate(Avg('visitorScore'))

    return render(request, 'racket/racketDetail.html', {'racketItems': getRacket,
                                                        'racketDetailItems': getRacketDetail,
                                                        'racketReviewForm': getReviewForm,
                                                        'racketReivewListItems': getReivewList,
                                                        'racketAvgScoreItem': getAvgScore
                                                        })

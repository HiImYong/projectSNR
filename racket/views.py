from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Avg, Func, FloatField, F
from django.http import HttpRequest, request
from django.shortcuts import render, redirect, get_object_or_404

import visitor.forms
from racket.models import Racket, RacketDetail
from visitor.models import VisitorReview


def racketMain(request: HttpRequest):
    getSearchKeyword = request.GET.get('searchKeyword', '')
    sort = request.GET.get('sort', '')
    page = request.GET.get('page', '1')

    if getSearchKeyword:
        getRacket = Racket.objects.filter(name__icontains=getSearchKeyword).order_by('name')
        getAdminScore = RacketDetail.objects.get(racket_id=1)
        getAvgScore = VisitorReview.objects.filter(visitorRacket_id=1).aggregate(Avg('visitorScore'))

    else:
        if sort == 'names':
            getRacket = Racket.objects.order_by('name')
            getAvgScore = VisitorReview.objects.filter(visitorRacket_id=1).aggregate(Avg('visitorScore'))
        elif sort == 'id' or '':
            getRacket = Racket.objects.order_by('id')
            getAvgScore = VisitorReview.objects.filter(visitorRacket_id=1).aggregate(Avg('visitorScore'))
        else:
            getRacket = Racket.objects.order_by('name')
            getAvgScore = VisitorReview.objects.filter(visitorRacket_id=1).aggregate(Avg('visitorScore'))

    paginator = Paginator(getRacket, 10)  # 페이지당 10개씩 보여주기
    getRacket = paginator.get_page(page)

    return render(request, "racket/racketMain.html", {'racketItems': getRacket,
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


def like(request, parameter):
    getRacketQs = Racket.objects.filter(id=parameter)
    getRacket = getRacketQs.first()
    getRacket.like.add(request.user)
    return redirect('racket:racketDetail', parameter=parameter)




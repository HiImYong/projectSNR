from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Avg, Func, FloatField, F, Count
from django.http import HttpRequest, request
from django.shortcuts import render, redirect, get_object_or_404

import visitor.forms
from racket.models import Racket, RacketDetail, RacketBrand
from visitor.models import VisitorReview


def racketMain(request: HttpRequest):
    getBrand = RacketBrand.objects.all()
    getSearchKeyword = request.GET.get('searchKeyword', '')
    sortBrandId = request.GET.get('sortBrand', '')
    sort = request.GET.get('sort', '')
    page = request.GET.get('page', '1')


    if getSearchKeyword:
        getRacket = Racket.objects.filter(name__icontains=getSearchKeyword).order_by('name')
        paginator = Paginator(getRacket, 10)  # 페이지당 10개씩 보여주기
        page = request.GET.get('page')
        getRacket = paginator.get_page(page)

        return render(request, "racket/racketMain.html", {'racketItems': getRacket,
                                                          'racketBrandItems': getBrand})

    elif sortBrandId:
        getRacket = Racket.objects.filter(brand_id=sortBrandId).order_by('name')

        paginator = Paginator(getRacket, 10)  # 페이지당 10개씩 보여주기
        getRacket = paginator.get_page(page)

        return render(request, "racket/racketMain.html", {'racketItems': getRacket,
                                                          'racketBrandItems': getBrand})

    else:
        if sort == 'names':
            getRacket = Racket.objects.order_by('name')
        elif sort == 'adminScore':
            getRacket = Racket.objects.order_by(F('detail__adminAvgScore').desc(nulls_last=True))
        elif sort == 'visitorScore':
            getRacket = Racket.objects.order_by(F('visitorAvgScore').desc(nulls_last=True))
        elif sort == 'countLike':
            getRacket = Racket.objects.order_by(F('countLike').desc(nulls_last=True))

        # elif sort == 'WILSON':
        #     getRacket = Racket.objects.filter(manufacturer__icontains='WILSON').order_by('name')


        else:
            getRacket = Racket.objects.order_by('name')

        paginator = Paginator(getRacket, 10)  # 페이지당 10개씩 보여주기
        getRacket = paginator.get_page(page)

        return render(request, "racket/racketMain.html", {'racketItems': getRacket,
                                                          'racketBrandItems': getBrand})


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


def like(request, parameter, self=None):
    getRacketQs = Racket.objects.filter(id=parameter) # 딕셔너리 변수에 파라미터를 받아와 라켓들 넣어줌
    getRacket = getRacketQs.first() # 혹시 모르니까 첫번째 라켓만 딕셔너리에서 빼냄
    checkUser = getRacket.like.filter(id=request.user.id)  # name이 와서는 안되나요? # 리퀘스트와 함께 온 라켓정보와 유저 정보 중 디비를 뒤져서 id를 통해 좋아요한 유저 빼냄.
    if checkUser.exists():  # 만약에 해당 라켓에 이전에 그 유저가 좋아요를 했다면
        getRacket.like.remove(request.user)  # 해당 유저 정보를 삭제함. 이 때
    else:
        getRacket.like.add(request.user)
        getLikeCount = getRacket.like.all().aggregate(Count('id'))['id__count']
        print(getLikeCount)
        getRacket.countLike = getLikeCount
        getRacket.save(self)

    return redirect('racket:racketDetail', parameter=parameter)

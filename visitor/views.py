from django.contrib import messages
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, resolve_url

# Create your views here.
from racket.models import Racket
from visitor.forms import ReviewForm
from visitor.models import VisitorReview


def newReview(request, parameter):
    if request.method == "POST":
        getForm = ReviewForm(request.POST)

        if getForm.is_valid():
            savedReview = getForm.save(commit=False)
            savedReview.visitorAccount = request.user
            savedReview.visitorRacket_id = parameter
            savedReview.save()
            messages.success(request, "리뷰가 등록되었습니다")
            return redirect('{}#anchor{}'.format(resolve_url('racket:racketDetail', parameter=parameter), 1))

    else:
        getForm = ReviewForm()


def modifyReview(request):
    jsonObject = json.loads(request.body)
    getReview = VisitorReview.objects.filter(id=jsonObject.get('id'))
    context = {
        'result': 'no'
    }
    if getReview is not None:
        getReview.update(visitorReview=jsonObject.get('content'))
        context = {
            'result': 'ok'
        }
        return JsonResponse(context)
    return JsonResponse(context)
#
#
# def deleteReview(request, parameter):
#     return None

from django.contrib import messages
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, resolve_url

# Create your views here.
from django.views.decorators.http import require_POST

from racket.models import Racket
from visitor.forms import ReviewForm
from visitor.models import VisitorReview


@require_POST
def newReview(request, parameter):
    getRacketQs = Racket.objects.filter(id=parameter)
    getRacket = getRacketQs.first()

    if request.method == "POST":
        getForm = ReviewForm(request.POST)

        if getForm.is_valid():
            savedText = getForm.cleaned_data['visitorReview']
            savedScore = getForm.cleaned_data['visitorScore']

            VisitorReview.objects.create(visitorAccount=request.user, visitorReview=savedText,
                                         visitorRacket_id=parameter, visitorScore=savedScore)
            messages.success(request, "리뷰가 등록되었습니다")
            return redirect('{}#anchor{}'.format(resolve_url('racket:racketDetail', parameter=parameter), 9999))

        else:
            return redirect('{}#anchor{}'.format(resolve_url('racket:racketDetail', parameter=parameter), 9999))

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

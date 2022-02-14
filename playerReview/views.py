from django.contrib import messages
from django.shortcuts import render, redirect, resolve_url

# Create your views here.
from django.views.decorators.http import require_POST

from player.models import Player
from playerReview.forms import ReviewForm
from playerReview.models import PlayerReviewModel


@require_POST
def newPlayerReview(request, parameter):
    if request.method == "POST":
        getForm = ReviewForm(request.POST)

        if getForm.is_valid():
            savedText = getForm.cleaned_data['visitorReview']

            PlayerReviewModel.objects.create(visitorAccount=request.user,
                                             visitorReview=savedText,
                                             visitorPlayer_id=parameter)

            messages.success(request, "리뷰가 등록되었습니다")
            print("저장완료")
            return redirect('{}#anchor{}'.format(resolve_url('player:playerDetail', parameter=parameter), 9998))

        else:
            print("저장실패")
            return redirect('{}#anchor{}'.format(resolve_url('player:playerDetail', parameter=parameter), 9998))

    else:
        getForm = ReviewForm()

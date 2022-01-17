from django.contrib import messages
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


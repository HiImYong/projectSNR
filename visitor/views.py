from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from racket.models import Racket
from visitor.forms import ReviewForm


def newReview(request, parameter):
    getRacket = Racket.objects.get(id=parameter)
    if request.method == "POST":
        getForm = ReviewForm(request.POST)

    if getForm.is_valid():
        savedReview = getForm.save(commit=False)
        savedReview.visitorAccount = request.user
        savedReview.visitorRacket = getRacket.id
        savedReview.save()
        messages.success(request, "리뷰가 등록되었습니다")
        return redirect('racket:racketDetail', parameter=getRacket.id)
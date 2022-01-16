from django.urls import path

from . import views

app_name = 'visitor'

urlpatterns = [
    path('visitor/<int:parameter>', views.newReview, name='newReview'),
]

#  urlpatterns 틀리면 안됨.

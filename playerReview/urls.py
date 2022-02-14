from django.urls import path

from . import views

app_name = 'playerReview'

urlpatterns = [
    path('player/<int:parameter>', views.newPlayerReview, name='newPlayerReview'),
    # path('player/modifyReview/', views.modifyReview, name='modifyReview'),
    # path('racketDetail/deleteReview', views.deleteReview, name='deleteReview')


]
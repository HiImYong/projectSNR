from django.urls import path

from . import views

app_name = 'racket'

urlpatterns = [
    path('', views.racketMain, name='racketMain'),
    path('racketDetail/<parameter>', views.racketDetail, name='racketDetail'),
    path('like/racket/<parameter>/', views.like, name='like'),

]
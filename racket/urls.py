from django.urls import path

from . import views

app_name = 'racket'

urlpatterns = [
    path('', views.racketMain, name='racketMain'),
    path('racketDetail/<int:parameter>', views.racketDetail, name='racketDetail'),
    path('like/racket/<int:parameter>/', views.like, name='like'),

]
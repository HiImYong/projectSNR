from django.urls import path
from . import views

app_name = 'racket'

urlpatterns = [
    path('', views.racketMain, name='racketMain')
]
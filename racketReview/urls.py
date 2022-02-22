from django.urls import path

from . import views

app_name = 'racketReview'

urlpatterns = [
    path('racketReview/<int:parameter>', views.newReview, name='newReview'),
    path('racketReview/modifyReview/', views.modifyReview, name='modifyReview'),
    path('racketDetail/deleteReview', views.deleteReview, name='deleteReview')


]

#  urlpatterns 틀리면 안됨.

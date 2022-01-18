from django.urls import path

from . import views

app_name = 'visitor'

urlpatterns = [
    path('visitor/<int:parameter>', views.newReview, name='newReview'),
    path('visitor/modifyReview/', views.modifyReview, name='modifyReview'),
    # path('visitor/delete/<int:parameter>', views.deleteReview, name='deleteReview'),

]

#  urlpatterns 틀리면 안됨.

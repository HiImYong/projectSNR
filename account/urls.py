from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('logOut/', views.logOut, name='logOut'),
    path('kakaoLogin/', views.kakaoLogin, name='kakaologin'),
    path('kakaoLoginCallBack/', views.kakaoLoginCallBack, name='kakaoLoginCallBack')

]

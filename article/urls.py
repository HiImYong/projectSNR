from django.urls import path

from . import views

app_name = 'article'

urlpatterns = [
    path('', views.articleMain, name='articleMain'),
    path('articleCreate/', views.articleCreate, name='articleCreate'),
    path('articleContent/<int:parameter>/', views.articleContent, name='articleContent'),
    path('articleContent/replyCreate/<int:parameter>/', views.replyCreate, name='replyCreate'),


]
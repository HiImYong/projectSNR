from django.urls import path
from . import views

app_name = 'player'

urlpatterns = [
    path('playerMain/', views.playerMain, name='playerMain'),
]

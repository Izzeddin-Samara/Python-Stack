from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('guess', views.guess, name='guess'),
    path('play_again', views.play_again, name='play_again'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('save_winner', views.save_winner, name='save_winner'),
]

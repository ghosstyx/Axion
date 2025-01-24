from main.urls import path
from index.views import *

urlpatterns = [
    path('<int:pk>/', index, name='index'),
    path('leaderboard/<int:pk>/', leaderboard, name='leaderboard'),
]

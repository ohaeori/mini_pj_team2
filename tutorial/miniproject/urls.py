from django.urls import path
from . import views
urlpatterns = [
    path('league/', views.league),
    path('player/', views.player),
    path('comment/', views.comment),
    path('news/', views.news),
    path('news_board/', views.news_board),
]
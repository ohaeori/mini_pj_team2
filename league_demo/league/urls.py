from django.urls import path
from . import views

urlpatterns = [
   
    path('player/', views.player_search),  # 추천순 정렬 url
    path('club/', views.select_club),
    path('club/<str:c_name>/', views.club_info),
    path('main/<str:date>/', views.main),
    path('news/', views.news),
    path('', views.index),
]
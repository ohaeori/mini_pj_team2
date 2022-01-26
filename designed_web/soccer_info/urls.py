from django.urls import path,include
from . import views

appname='soccer_info'
urlpatterns = [
    #path('', views.index, name='index'),
    ######### 리그 별로 정리되어야 함!!!!!!!!!
    path('', ), # 메인페이지1
    path('main_page/', views.main_page, name="main_page"), # 메인페이지2
    path('club_intro/', views.club_intro, name="club_intro"), # 클럽정보(첫페이지)
    path('club_info/<str:club_name>', views.club_info, name="club_info"), # 클럽정보(클럽 선택 후 페이지)
    path('schedule/', views.schedule, name="schedule"), # 일정/결과
    path('rank/', views.rank, name="rank"), # 순위
    path('search_player', views.search_player, name="search_player"), # 선수 검색
]
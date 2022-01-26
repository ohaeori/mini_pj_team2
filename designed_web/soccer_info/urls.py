from django.urls import path,include
from . import views

appname='soccer_info'
urlpatterns = [
    #path('', views.index, name='index'),
    path('', ), # 메인페이지1
    path('', ), # 메인페이지2
    path('', ), # 클럽정보(첫페이지)
    path('', ), # 클럽정보(클럽 선택 후 페이지)
    path('', ), # 일정/결과
    path('', ), # 순위
    path('', ), # 선수 검색
]
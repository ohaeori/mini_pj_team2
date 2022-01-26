from django.urls import path,include
from . import views

appname='soccer_news'
urlpatterns = [
    #path('', views.index, name='index'),
    path('', ), # 뉴스 첫페이지(최신순 정렬)1
    path('', ), # 뉴스 첫페이지(최신순 정렬)2
    path('', ), # 뉴스 두번째 페이지(댓글순 정렬)
    path('', ), # 커뮤니티 첫페이지(댓글순 정렬)
]
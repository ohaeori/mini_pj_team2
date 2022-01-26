from django.urls import path,include
from . import views

appname='soccer_news'
urlpatterns = [
    #path('', views.index, name='index'),
    path('', ), # 뉴스 첫페이지(최신순 정렬)1
    path('intro_sorted_date', views.intro_sorted_date, name="intro_sorted_date" ), # 뉴스 첫페이지(최신순 정렬)2
    path('intro_sorted_comment', views.intro_sorted_comment, name="intro_sorted_comment"), # 뉴스 두번째 페이지(댓글순 정렬)
]
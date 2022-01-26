from django.urls import path,include
from . import views

appname='cummunity'
urlpatterns = [
    #path('', views.index, name='index'),
    path('', ), # 커뮤니티 첫페이지(최신순 정렬)1
    path('intro_sorted_date/', views.intro_sorted_date, name="intro_sorted_date"), # 커뮤니티 첫페이지(최신순 정렬)2
    path('intro_sorted_good/', views.intro_sorted_good, name="intro_sorted_date"), # 커뮤니티 첫페이지(추천순 정렬)
    path('intro_sorted_comment/', views.intro_sorted_comment, name="intro_sorted_date"), # 커뮤니티 첫페이지(댓글순 정렬)
    path('my_page/', views.my_page, name = "my_page"), # 내가 쓴 글, 내가 쓴 댓글
    path('good_page/', views.good_page, name="good_page"), # 추천한 글
    path('editer_page/', views.editer_page, name = "editer_page"), # 글쓰기
    path('post_view/<int:post_num>/', views.post_view, name = "post_view"), # 게시물 확인
]
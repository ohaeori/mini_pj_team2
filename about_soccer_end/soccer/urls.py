from django.urls import path,include

from . import views

appname='soccer'
urlpatterns = [
    #path('', views.index, name='index'),
    #path('', views.login_custom, name='login_custom'),
    path('signup/custom/', views.signup_custom, name='signup_custom'),

    # 내가 쓴 글 보기#
    path('comment/', views.comment),
    # 커뮤니티 첫 화면들 #
    path('community_sorted_date/', views.community_sorted_date, name='community_sorted_date'),
    path('community_sorted_good/', views.community_sorted_good, name='community_sorted_good'),
    path('community_sorted_comment/', views.community_sorted_comment, name='community_sorted_comment'),
    path('logout/custom/', views.logout_custom, name='logout_custom'), #로그아웃
    # 게시글 확인 #
    path('community_sorted_date/<int:pk>/', views.posting, name='posting1'),
    path('community_sorted_good/<int:pk>/', views.posting, name='posting2'),
    path('community_sorted_comment/<int:pk>/', views.posting, name='posting3'),
    # 게시글 삭제 #
    # 게시글 작성 #
    path('community_sorted_date/create_notice/', views.create_notice),

    path('community/notice_list/', views.notice_list, name='notice_list'),
    # path('community/notice_list/create_notice/', views.create_notice),
    path('community/notice_list/<int:pk>/', views.posting,name='posting'),


    path('player/<str:l_name>/<str:date>/', views.player_search), #-- 변경
    path('club/<str:l_name>/<str:date>/', views.select_club),
    path('club/<str:l_name>/<str:date>/<str:c_name>/', views.club_info),
    path('main/<str:l_name>/<str:date>/', views.main),
    path('news/', views.news),
    path('', views.index),
]
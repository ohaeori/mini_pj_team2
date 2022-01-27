from django.urls import path,include

from . import views

appname='soccer'
urlpatterns = [
    #path('', views.index, name='index'),
    #path('', views.login_custom, name='login_custom'),
    path('logout/custom/', views.logout_custom, name='logout_custom'),
    path('signup/custom/', views.signup_custom, name='signup_custom'),
    path('comment/', views.comment),
    path('community/', views.community, name='index'),
    path('community/notice_list/', views.notice_list, name='notice_list'),
    path('community/notice_list/create_notice/', views.create_notice),
    path('community/notice_list/<int:pk>/', views.posting,name='posting'),
    path('community/notice_list/<int:pk>/delete_notice/', views.delete_notice),
    path('player/<str:l_name>/<str:date>/', views.player_search), #-- 변경
    path('club/<str:l_name>/<str:date>/', views.select_club),
    path('club/<str:l_name>/<str:date>/<str:c_name>/', views.club_info),
    path('main/<str:l_name>/<str:date>/', views.main),
    path('news/', views.news),
    path('', views.index),
]
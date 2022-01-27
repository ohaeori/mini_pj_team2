from django.urls import path,include

from . import views

app_name = 'community'
urlpatterns = [
    path('', views.index, name='index'),
    path('notice_list/', views.notice_list, name='notice_list'),
    path('notice_list/create_notice/', views.create_notice),
    path('notice_list/<int:pk>/', views.posting,name='posting'),
    path('notice_list/<int:pk>/delete_notice/', views.delete_notice),
    path('make_comment/', views.make_comment),
    path('orderdate/', views.order_by_date),  # 최신순 정렬 url
    path('ordergood/', views.order_by_good),  # 추천순 정렬 url
    path('ordercom/', views.order_by_comment),  # 추천순 정렬 url
    path('line/', views.user),
    path('signup/custom/', views.signup_custom, name='signup_custom'),
    path('login/custom/', views.login_custom, name='login_custom'),
    path('logout/custom/', views.logout_custom, name='logout_custom'),
    path('league/', views.league),
    path('player/', views.player),
    path('comment/', views.comment),
    path('news/', views.news),
    path('news_board/', views.news_board),
]
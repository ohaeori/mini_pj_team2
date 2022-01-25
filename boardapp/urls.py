from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.com),  #그냥 출력해본 url
    path('orderdate/', views.order_by_date),  # 최신순 정렬 url
    path('ordergood/', views.order_by_good),  # 추천순 정렬 url
    path('ordercom/', views.order_by_comment),  # 추천순 정렬 url

]
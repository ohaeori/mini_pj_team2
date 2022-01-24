from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('notice_list/', views.notice_list, name='notice_list'),
]
from django.urls import path,include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('community/', views.community, name='index'),
    path('community/notice_list/', views.notice_list, name='notice_list'),
    path('community/notice_list/create_notice/', views.create_notice),
    path('community/notice_list/<int:pk>/', views.posting,name='posting'),
    path('community/notice_list/<int:pk>/delete_notice/', views.delete_notice),
]
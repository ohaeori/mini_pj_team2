from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('notice_list/', views.notice_list, name='notice_list'),
    path('notice_list/create_notice/', views.create_notice),
    path('notice_list/<int:pk>/', views.posting,name='posting'),
    path('notice_list/<int:pk>/delete_notice/', views.delete_notice),
]
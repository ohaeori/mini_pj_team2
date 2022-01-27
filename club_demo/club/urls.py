from django.urls import path,include

from . import views

appname='soccer'
urlpatterns = [
    path('', views.select_club),
    path('<str:c_name>/', views.club_info),
    
]
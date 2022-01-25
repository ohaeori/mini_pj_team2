"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from firstapp import views
#from . import views
from . import views as config_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ # 분기 시켜줌
    path('admin/', admin.site.urls),
    path('index1/', views.index1),
    path('index2/', views.index2),
    path('first/', include('firstapp.urls')),
    path('home/', config_views.home),
    path('second/', include('secondapp.urls')),
    path('third/', include('thirdapp.urls')),
    path('text/<str:char>/',config_views.text),
    path('<int:year>/<int:month>/',config_views.date),
    path('search/', config_views.search),
    path('info/', config_views.info),
    path('member/', include('member.urls')),
    path('paging/', include('paging.urls')),
    path('file/', include('file.urls')),

    path('board/', include('boardapp.urls')),
    

]+ static(
settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)

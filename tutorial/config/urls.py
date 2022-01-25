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
from django.urls import path,include
from firstapp import views
from . import views as views1
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index1/', views.index1),
    path('index2/', views.index2),
    path('home/', views1.home),
    path('main/', views.main),
    path('insert/', include('firstapp.urls')),
    path('show/', include('firstapp.urls')),
    path('first/',include('firstapp.urls')),
    path('second/',include('secondapp.urls')),
    path('third/',include('thirdapp.urls')),
    path('mini/',include('miniproject.urls')),
    path('member/',include('member.urls')),
    path('paging/',include('paging.urls')),
    path('file/',include('file.urls')),
    path('text/<str:char>/',views1.text),
    path('<int:year>/<int:month>/',views1.date),
    path('search/',views1.search),
    path('info/',views1.info),

] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

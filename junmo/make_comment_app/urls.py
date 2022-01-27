from django.urls import path
from . import views
urlpatterns = [ 
    path('view_comment/', views.view_comment),
    path('make_comment/', views.make_comment),
    path('delete_comment/', views.delete_comment),
]
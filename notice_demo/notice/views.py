from django.shortcuts import render
from .models import Notice

# Create your views here.
def index(request):
    return render(request,'notice/index.html')

def notice_list(request): 
    notice_list=Notice.objects.all()
    return render(request, 'notice/notice_list.html',{'notice_list':notice_list})
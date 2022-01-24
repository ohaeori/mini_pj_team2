from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'notice/index.html')

def notice_list(request): return render(request, 'notice/notice_list.html')
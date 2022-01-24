from django.shortcuts import redirect, render
from .models import Notice

# Create your views here.
#처음화면
def index(request):
    return render(request,'notice/index.html')

#게시글 목록 표시
def notice_list(request): 
    notice_list=Notice.objects.all()
    return render(request, 'notice/notice_list.html',{'notice_list':notice_list})

#게시글 작성
def create_notice(request):
    if request.method == 'POST':
        new_article=Notice.objects.create(
                postname=request.POST['title'],
                contents=request.POST['contents'],
            )
        return redirect('/notice_list/')
    return render(request, 'notice/create_notice.html')
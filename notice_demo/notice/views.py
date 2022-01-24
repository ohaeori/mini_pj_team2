from django.shortcuts import redirect, render
from matplotlib.pyplot import title
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
        if request.POST['mainphoto']:
            new_article=Notice.objects.create(
                title=request.POST['title'],
                contents=request.POST['contents'],
            )
        else:
            new_article=Notice.objects.create(
                title=request.POST['title'],
                contents=request.POST['contents'],
            )
        return redirect('/notice_list/')
    return render(request, 'notice/create_notice.html')

#게시글 등록
def posting(request,pk):
    poster=Notice.objects.get(pk=pk)
    return render(request,'notice/posting.html',{'poster':poster})

#게시글 삭제
def delete_notice(request, pk):
    poster = Notice.objects.get(pk=pk)
    if request.method == 'POST':
        poster.delete()
        return redirect('/notice_list/')
    return render(request, 'notice/delete_notice.html', {'poster': poster})

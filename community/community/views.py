from django.utils import timezone
from django.shortcuts import redirect, render
from sqlalchemy import null
from .models import BOARD_TITLE

# Create your views here.
#처음화면
def index(request):
    return render(request,'community/index.html')

#게시글 목록 표시
def notice_list(request): 
    notice_list=BOARD_TITLE.objects.all()
    return render(request, 'community/notice_list.html',{'notice_list':notice_list})

#게시글 작성
def create_notice(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('url')
        if(upload_file): 
            name = upload_file.name
            with open('media/%s' % name, 'wb') as file:
                for chunk in upload_file.chunks():
                    file.write(chunk)
        else : name="null"        

        BOARD_TITLE.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            url=name,
            b_id=1,
            date=timezone.now()
        )
        return redirect('/notice_list/')
    return render(request, 'community/create_notice.html')

#게시글 보기
def posting(request,pk):
    poster=BOARD_TITLE.objects.get(pk=pk)
    return render(request,'community/posting.html',{'poster':poster})


#게시글 삭제
def delete_notice(request, pk):
    poster = BOARD_TITLE.objects.get(pk=pk)
    if request.method == 'POST':
        poster.delete()
        return redirect('/notice_list/')
    return render(request, 'community/delete_notice.html', {'poster': poster})
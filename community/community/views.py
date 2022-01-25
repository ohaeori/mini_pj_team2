from django.utils import timezone
from django.shortcuts import redirect, render
from sqlalchemy import null
from django.http import HttpResponse
from .models import BOARD_TITLE, COMMENT, USER

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

def make_comment(request):
    #임시로 로그인 한 척
    request.session['u_id_col'] = 'user4'
    # if user.is_authenticated: # 장고 기본기능이면 이걸 가져와야할 듯
    if request.method == 'POST':
        if request.POST.get('input_comment'):

            board_id = 1 # 게시판 번호는 해당 게시글 url에서 가져올 수 있도록 해야함
            title_id = BOARD_TITLE.objects.filter(t_num = 1)[0] # 마찬가지로 url에서 가져와야함
            user_id = USER.objects.get(u_id = request.session['u_id_col']) #로그인 상태의 유저 아이디를 가져옴
            comment_txt = request.POST.get('input_comment')
            
            one_comment = COMMENT(
                b_id = board_id,
                board_title = title_id,
                u_id_col = user_id,
                comment = comment_txt)
            one_comment.save()
            return redirect('/make_comment/')

    
    return render(request,'community/comment_box.html',)


#게시글 보기
def posting(request,pk):
    poster=BOARD_TITLE.objects.get(pk=pk)
    make_comment(request)#t_num=poster.t_num
    comment_list = COMMENT.objects.filter(board_title=poster)
    return render(request,'community/posting.html',{'poster':poster,'comment_list': comment_list})


#게시글 삭제
def delete_notice(request, pk):
    poster = BOARD_TITLE.objects.get(pk=pk)
    if request.method == 'POST':
        poster.delete()
        return redirect('/notice_list/')
    return render(request, 'community/delete_notice.html', {'poster': poster})

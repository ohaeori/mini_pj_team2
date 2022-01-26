from django.utils import timezone
from django.shortcuts import redirect, render
from sqlalchemy import null
from django.http import HttpResponse
from .models import BOARD_TITLE, COMMENT, USER, LEAGUE, PLAYER, NEWS, NEWS_COMMENT
import collections

# Create your views here.
#처음화면
def index(request):
    return render(request,'community/index.html')

def order_by_comment(request): #댓글 순 정렬
    dic_com = {}
    b = BOARD_TITLE.objects.all()
    for i in range(len(BOARD_TITLE.objects.all())): # i=> t_num
        dic_com[BOARD_TITLE.objects.all()[i].t_num] = b[i].comment_set.count() #댓글수
    # com_list =  Board_title.objects.values('t_num').annotate(cnt = Count('t_num')).order_by('-cnt')
    sorted_by_value = sorted(dic_com.items(), key=lambda x: x[1], reverse=True)

    sorted_dict = collections.OrderedDict(sorted_by_value)
  
    list_value1 = []
    list_value2 = []
    for k, v in sorted_dict.items():
        list_value1.append(k)
        list_value2.append(v)

    d = {}
    title_list=[]
    for i in range(len(BOARD_TITLE.objects.all())):
        d[BOARD_TITLE.objects.all()[i].t_num] = BOARD_TITLE.objects.all()[i].title

    for c in list_value1:
        for key, value in d.items(): 
            if c == key:
                title_list.append(value)
         
    return (list_value1,list_value2,title_list)
   

#게시글 목록 표시
def notice_list(request): 
    notice_list=BOARD_TITLE.objects.all()
    write_date_list=notice_list.order_by('-date')
    good_list =notice_list.order_by('-good')
    order=order_by_comment(request)
    list_value1,list_value2,title_list=order
    return render(request, 'community/notice_list.html',{'notice_list':notice_list,'write_date_list':  write_date_list,'good_list':  good_list
    ,'com_list':  list_value1, 'title_list': title_list, 'cnt_list':  list_value2,'order':order  })

def order_by_date(request): #날짜 순 정렬
   write_date_list =  BOARD_TITLE.objects.all().order_by('-date')
   return render(request,'community/orderdate.html',{'write_date_list':  write_date_list }
   ) 

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
    #request.session.flush()
    
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


      

def order_by_good(request): #추천 순 정렬
   good_list =  BOARD_TITLE.objects.all().order_by('-good')
   return render(
        request,
        'community/ordergood.html',
        {'good_list':  good_list }
   )


# user 출력
def user(request):
   user_list = USER.objects.all()
   return render(
        request,
        'community/line.html',
        {'user_list': user_list }
   )

from .models import USER
from django.utils import timezone
from django.http import HttpResponse

#회원가입
def signup_custom(request):
    if request.method == 'POST':
        user_id = request.POST.get('u_id')
        user_pw = request.POST.get('pw')
        user_name = request.POST.get('u_name')
        birth_date = request.POST.get('birth_date')
        nickname = request.POST.get('nickname')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')

        u = USER(
            u_id=user_id, pw=user_pw, u_name=user_name, 
            birth_date=birth_date, nickname=nickname, phone_num=phone_num, email=email)
        u.date_joined = timezone.now()
        u.save()
        return HttpResponse(
            '가입 완료<br>%s %s %s' % (user_id, user_pw, user_name))
    else:
        return render(request, 'community/signup_custom.html')

#로그인
def login_custom(request):
    user_list = USER.objects.all()
    if request.method == 'POST':
        user_id = request.POST.get('u_id')
        user_pw = request.POST.get('pw')
        try:
            u = USER.objects.get(u_id=user_id, pw=user_pw)
            # 회원정보 조회 실패 시 예외 발생
        except:
            return HttpResponse('로그인 실패')
        else: #로그인 판단 요소 ==> 나중에 이걸로 다양한 정보 확인(동현에이블러님 활용)
            request.session['u_id'] = u.u_id
            request.session['u_name'] = u.u_name
        return render(
        request,
        'community/login_custom.html',
        {'user_list': user_list }
    )   
      
    else:
        return render(request, 'community/login_custom.html')

#로그아웃
def logout_custom(request):
    del request.session['u_id'] # 개별 삭제
    del request.session['u_name'] # 개별 삭제
    request.session.flush() # 전체 삭제
    return redirect('coummnity:login_custom')

def league(request):
    league = LEAGUE.objects.all()
    result = ''
    for i in league:
        result+=i.l_name+'<br>'
    return HttpResponse(result)
    return render(
        request,'/league.html',
        {'data' : league}
        )

def player(request):
    player = PLAYER.objects.all()
    result = ''
    for i in player:
        result+=i.name+'<br>'
    return HttpResponse(result)
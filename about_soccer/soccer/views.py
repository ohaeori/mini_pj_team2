from django.utils import timezone
from django.shortcuts import redirect, render
from sqlalchemy import null
from django.http import HttpResponse
from .models import GAME, LEAGUE, PLAYER,CLUB,BOARD_TITLE,NEWS, COMMENT, USER,BOARD
from django.db.models import Count
import datetime
# Create your views here.
#처음화면


def community(request):
    return render(request,'soccer/community.html')

def order_by_comment(request):
    comment_list = COMMENT.objects.values("board_title").annotate(count_board = Count("c_id")).order_by('-count_board')
    # for i in comment_list:
    #     print(i)
    #     print(type(i))
    '''
    {게시글 번호}, {댓글 수}
    {'board_title': 1, 'count_board': 14}
    {'board_title': 8, 'count_board': 3}
    {'board_title': 2, 'count_board': 2}
    {'board_title': 3, 'count_board': 2}
    {'board_title': 4, 'count_board': 2}
    {'board_title': 5, 'count_board': 2}
    {'board_title': 6, 'count_board': 2}
    {'board_title': 7, 'count_board': 2}
    {'board_title': 10, 'count_board': 2}
    {'board_title': 9, 'count_board': 1}
    '''
    board_num = []
    board_data = []
    for i in comment_list:
        board_num.append(i)
        board_data.append(BOARD_TITLE.objects.get(t_num = i['board_title']))
        # print(i['board_title'])
        # print(BOARD_TITLE.objects.get(t_num = i['board_title']).title)

    return zip(board_num , board_data)

   




#게시글 목록 표시
def notice_list(request): 
    notice_list=BOARD_TITLE.objects.all()
    write_date_list=notice_list.order_by('-date')
    good_list =notice_list.order_by('-good')
    order=order_by_comment(request)
    zip_board=order
    return render(request, 'soccer/notice_list.html',{'notice_list':notice_list,'write_date_list':  write_date_list,'good_list':  good_list
    ,'zip_board':  zip_board})

#게시글 작성
def create_notice(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('url')
        if(upload_file): 
            name = upload_file.name
            with open('static/media/%s' % name, 'wb') as file:
                for chunk in upload_file.chunks():
                    file.write(chunk)
        else : name="null"        

        BOARD_TITLE.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            user=USER.objects.get(u_id=request.session['u_id']),
            url=name,
            board=BOARD.objects.get(b_name='자유게시판'),
            date=timezone.now()
        )
        return redirect('/community/notice_list/')
    return render(request, 'soccer/create_notice.html')



def make_comment(request,pk):
    #임시로 로그인 한 척
    #request.session['u_id_col'] = 'user4'
    #request.session.flush()
    
    if request.method == 'POST':
        if request.POST.get('input_comment'):

            board_id = 1 # 게시판 번호는 해당 게시글 url에서 가져올 수 있도록 해야함
            title_id = BOARD_TITLE.objects.filter(t_num = pk)[0] # 마찬가지로 url에서 가져와야함
            user_id = USER.objects.get(u_id = request.session['u_id_col']) #로그인 상태의 유저 아이디를 가져옴
            comment_txt = request.POST.get('input_comment')
            
            one_comment = COMMENT(
                b_id = board_id,
                board_title = title_id,
                u_id_col = user_id,
                comment = comment_txt)
            one_comment.save()
            return redirect('/make_comment/')

    
    return render(request,'soccer/comment_box.html',)


#게시글 보기
def posting(request,pk):
    poster=BOARD_TITLE.objects.get(pk=pk)
    make_comment(request,pk)#t_num=poster.t_num
    comment_list = COMMENT.objects.filter(board_title=poster)
    return render(request,'soccer/posting.html',{'poster':poster,'comment_list': comment_list})


#게시글 삭제
def delete_notice(request, pk):
    poster = BOARD_TITLE.objects.get(pk=pk)
    if request.method == 'POST':
        poster.delete()
        return redirect('/community/notice_list/')
    return render(request, 'soccer/delete_notice.html', {'poster': poster})





# user 출력
def user(request):
   user_list = USER.objects.all()
   return render(
        request,
        'soccer/line.html',
        {'user_list': user_list }
   )


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
        return redirect('../../')
    else:
        return render(request, 'soccer/signup_custom.html')

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
            request.session['u_id_col'] = user_id
        return render(request,'soccer/login_custom.html',{'user_list': user_list }
    )   
      
    else:
        return render(request, 'soccer/login_custom.html')

#로그아웃
def logout_custom(request):
    del request.session['u_id'] # 개별 삭제
    del request.session['u_name'] # 개별 삭제
    request.session.flush() # 전체 삭제
    return redirect('../../')


def comment(request):
    id=request.session['u_id']
    comment = COMMENT.objects.filter(u_id_col__u_id__contains = id)
    title = BOARD_TITLE.objects.filter(user__u_id__contains = id)
    return render(
        request,'soccer/comment.html',
        {'comment' : comment, 'title' : title,}
    )

def player_search(request):
    P_list = PLAYER.objects.all() # 처음에는 모든 선수 정보를 출력하도록 함

    posi_list = PLAYER.objects.filter()

    if request.method == 'POST':

        if request.POST.get('club'):
            club = request.POST.get('club')
            P_list = P_list.filter(club = club)


        if request.POST.get('name'):
            name = request.POST.get('name')
            P_list = P_list.filter(p_name__contains = name)

        if request.POST.get('position'):
            po = request.POST.get('position')
            if po == 'all':
                P_list = P_list.all()
            else:
                P_list = P_list.filter(position = po)

        if request.POST.get('country'):
            coun = request.POST.get('country')
            P_list = P_list.filter(country = coun)
            
    
    return render(
            request,
            'soccer/player.html',
            {'P_list':  P_list}
    )


def index(request):
    date1 = datetime.datetime.today()
    league_list=LEAGUE.objects.all()
    return render(request,'soccer/index.html',{'date1':date1,'league_list':league_list})

def club_info(request,c_name,l_name):
    player_list=PLAYER.objects.filter(club__c_name__contains=c_name)
    schedule_list=GAME.objects.filter(home_team__contains=c_name ) |GAME.objects.filter(away_team__contains=c_name )
    
    return render(request,'soccer/club_info.html',{'club_name':c_name,'player_list':player_list,'schedule_list':schedule_list})

def select_club(request,l_name):
    club_list=CLUB.objects.filter(league__l_name__contains=l_name)
    return render(request,'soccer/select_club.html',{'club_list':club_list,'l_name':l_name})


def AddDays(sourceDate, count): 
    targetDate = sourceDate + datetime.timedelta(days = count) 
    return targetDate

def GetWeekFirstDate(sourceDate): 
    temporaryDate = datetime.datetime(sourceDate.year, sourceDate.month, sourceDate.day) 
    weekDayCount = temporaryDate.weekday() 
    targetDate = AddDays(temporaryDate, -weekDayCount); 
    return targetDate

# 메인페이지
def main(request,date,l_name):
    id = l_name
    date1 = datetime.datetime.today()
    first_date = GetWeekFirstDate(date1)
    news = NEWS.objects.filter(league = id)
    club = CLUB.objects.filter(league = id).order_by('rank')
    game = GAME.objects.filter(date__contains=date,LEAGUE=id)
    community = BOARD_TITLE.objects.all().order_by('-good')
    date2 = []
    for i in range(7):
        date2.append(AddDays(first_date,i).date)

    return render(request,'soccer/main.html',
    {'date2':date2,'news':news,'game':game,'club':club,'community':community,'l_name':l_name})

def news(request):
    news = NEWS.objects.all()
    return render(request,'soccer/news.html',{'news':news})
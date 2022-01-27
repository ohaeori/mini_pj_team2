from django.shortcuts import render
from .models import  GAME, LEAGUE, PLAYER,CLUB,BOARD_TITLE,NEWS
# Create your views here.
import datetime

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
            'league/player.html',
            {'P_list':  P_list}
    )


def index(request):
    date1 = datetime.datetime.today()
    return render(request,'league/index.html',{'date1':date1})

def club_info(request,c_name):
    player_list=PLAYER.objects.filter(club__c_name__contains=c_name)
    schedule_list=GAME.objects.filter(home_team__contains=c_name ) |GAME.objects.filter(away_team__contains=c_name )
    
    return render(request,'league/club_info.html',{'club_name':c_name,'player_list':player_list,'schedule_list':schedule_list})

def select_club(request):
    club_list=CLUB.objects.all()
    return render(request,'league/select_club.html',{'club_list':club_list})


def AddDays(sourceDate, count): 
    targetDate = sourceDate + datetime.timedelta(days = count) 
    return targetDate

def GetWeekFirstDate(sourceDate): 
    temporaryDate = datetime.datetime(sourceDate.year, sourceDate.month, sourceDate.day) 
    weekDayCount = temporaryDate.weekday() 
    targetDate = AddDays(temporaryDate, -weekDayCount); 
    return targetDate

# 메인페이지
def main(request,date):
    id = 'Premier League'
    date1 = datetime.datetime.today()
    first_date = GetWeekFirstDate(date1)
    news = NEWS.objects.filter(league = id)
    club = CLUB.objects.filter(league = id).order_by('rank')
    game = GAME.objects.filter(date__contains=date)
    community = BOARD_TITLE.objects.all().order_by('-good')
    date2 = []
    for i in range(7):
        date2.append(AddDays(first_date,i).date)

    return render(request,'league/main.html',
    {'date2':date2,'news':news,'game':game,'club':club,'community':community})

def news(request):
    news = NEWS.objects.all()
    return render(request,'league/news.html',{'news':news})
from django.utils import timezone
from django.shortcuts import redirect, render
from sqlalchemy import null
from django.http import HttpResponse
from datetime import datetime

from club.models import GAME, PLAYER,CLUB


def index(request):
    return render(request,'club/index.html')

def club_info(request,c_name):
    player_list=PLAYER.objects.filter(CLUB__c_name__contains=c_name)
    schedule_list=GAME.objects.filter(home_team__contains=c_name ) |GAME.objects.filter(away_team__contains=c_name )
    
    return render(request,'club/club_info.html',{'club_name':c_name,'player_list':player_list,'schedule_list':schedule_list})

def select_club(request):
    club_list=CLUB.objects.all()
    return render(request,'club/select_club.html',{'club_list':club_list})
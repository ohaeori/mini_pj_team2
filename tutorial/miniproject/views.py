from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Board_title, League,Player, Comment,News,News_Comment
from member.models import User
def league(request):
    league = League.objects.all()
    result = ''
    for i in league:
        result+=i.l_name+'<br>'
    return HttpResponse(result)
    return render(
        request,'miniproject/league.html',
        {'data' : league}
        )

def player(request):
    player = Player.objects.all()
    result = ''
    for i in player:
        result+=i.name+'<br>'
    return HttpResponse(result)

# def comment(request):
#     id = request.GET.get('id')
    
#     comment = Comment.objects.filter(u_id__contains = id)
#     # result = ''
#     # for i in comment:
#     #     result+=i.comment+'<br>'
#     return render(
#         request,'miniproject/comment.html',
#         {'data' : comment}
#     )
#     return HttpResponse(comment)


def comment(request):
    id=request.session['u_id']
    
    comment = Comment.objects.filter(u_id__contains = id)
    title = Board_title.objects.filter(u_id__contains = id)
    return render(
        request,'miniproject/comment.html',
        {'comment' : comment, 'title' : title,}
    )



def news(request):
    id = request.GET.get('id')
    news = News.objects.filter(n_id = id)
    comment = News_Comment.objects.filter(news = id)
    return render(
        request,'miniproject/news.html',
        {'comment' : comment, 'news' : news}
    )
    return HttpResponse(comment)

def news_board(request):
    news = News.objects.all()
    return render(
        request,'miniproject/news_board.html',
        {'news' : news}
    )
    return HttpResponse(comment)



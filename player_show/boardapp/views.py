from django.shortcuts import render
from matplotlib.pyplot import title
from .models import Comment, Board_title, Player, Club
# Create your views here.


def order_by_date(request): #날짜 순 정렬
   write_date_list =  Board_title.objects.all().order_by('-date')
   return render(
        request,
        'boardapp/orderdate.html',
        {'write_date_list':  write_date_list }
   )       

def order_by_good(request): #추천 순 정렬
   good_list =  Board_title.objects.all().order_by('-good')
   return render(
        request,
        'boardapp/ordergood.html',
        {'good_list':  good_list }
   )

from django.db.models import Count
# def order_by_comment(request): #댓글 순 정렬
#     com_list =  Comment.objects.values('t_num').annotate(cnt = Count('t_num')).order_by('-cnt')
#     list_value = []
#     for i in range(len(com_list)):
#         # print(com_list[i])
#         for k,v in com_list[i].items():
#             print(v, end = ' ')
#             list_value.append(v)

#     list_value1 = []
#     list_value2 = []
#     for i in range(len(list_value)):
#         if i % 2 == 0:
#             list_value1.append(list_value[i])
#         else:
#             list_value2.append(list_value[i])
#     d = {}
#     title_list = []

#     for i in range(len(Board_title.objects.all())):
#         d[Board_title.objects.all()[i].t_num] = Board_title.objects.all()[i].title

#     for c in list_value1:
#         for key, value in d.items(): 
#             if c == key:
#                 title_list.append(value)

#     return render(
#          request,
#          'boardapp/ordercom.html',
#          {'com_list':  list_value1, 'title_list': title_list, 'cnt_list':  list_value2,}
#    )

import collections

def order_by_comment(request): #댓글 순 정렬
    dic_com = {}
    b = Board_title.objects.all()
    for i in range(len(Board_title.objects.all())): # i=> t_num
        dic_com[Board_title.objects.all()[i].t_num] = b[i].comment_set.count() #댓글수
    # com_list =  Board_title.objects.values('t_num').annotate(cnt = Count('t_num')).order_by('-cnt')
    sorted_by_value = sorted(dic_com.items(), key=lambda x: x[1], reverse=True)

    sorted_dict = collections.OrderedDict(sorted_by_value)
    list_value1 = []
    list_value2 = []
    for k, v in sorted_dict.items():
        list_value2.append(v)
        list_value1.append(k)

    d = {}
    title_list = []

    for i in range(len(Board_title.objects.all())):
        d[Board_title.objects.all()[i].t_num] = Board_title.objects.all()[i].title

    for c in list_value1:
        for key, value in d.items(): 
            if c == key:
                title_list.append(value)
    return render(
         request,
         'boardapp/ordercom.html',
         {'com_list':  list_value1, 'title_list': title_list, 'cnt_list':  list_value2,}
   )

# select t_num, count(t_num) as cnt from COMMENT
# group by t_num order by cnt desc;             


# def com(request):
#    c_list = Comment.objects.all()
#    return render(
#         request,
#         'boardapp/comment.html',
#         {'c_list':  c_list }
#    )   

def player_search(request):
    P_list = Player.objects.all() # 처음에는 모든 선수 정보를 출력하도록 함

    posi_list = Player.objects.filter()

    if request.method == 'POST':

        if request.POST.get('club'):
            club = request.POST.get('club')
            P_list = P_list.filter(club = club)
            #P_list = Player.objects.filter(club = club)

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
            
    # if request.method == 'POST':
    #     if request.POST.get('club'):
    #         club = request.POST.get('club')
    #         P_list = Player.objects.filter(club = club)
    #     if request.POST.get('name'):
    #         name = request.POST.get('name')
    #         P_list = Player.objects.filter(p_name__contains = name)
    #     if request.POST.get('position'):
    #         po = request.POST.get('position')
    #         P_list = Player.objects.filter(position = po)
    #     if request.POST.get('country'):
    #         coun = request.POST.get('country')
    #         P_list = Player.objects.filter(country = coun)
            
    return render(
            request,
            'boardapp/player.html',
            {'P_list':  P_list}
    )




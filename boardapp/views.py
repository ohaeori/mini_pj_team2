from django.shortcuts import render
from matplotlib.pyplot import title
from .models import Comment, Board_title
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
def order_by_comment(request): #댓글 순 정렬
    com_list =  Comment.objects.values('t_num').annotate(cnt = Count('t_num')).order_by('-cnt')
    list_value = []
    for i in range(len(com_list)):
        # print(com_list[i])
        for k,v in com_list[i].items():
            print(v, end = ' ')
            list_value.append(v)

    list_value1 = []
    list_value2 = []
    for i in range(len(list_value)):
        if i % 2 == 0:
            list_value1.append(list_value[i])
        else:
            list_value2.append(list_value[i])
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


def com(request):
   c_list = Comment.objects.all()
   return render(
        request,
        'boardapp/comment.html',
        {'c_list':  c_list }
   )   



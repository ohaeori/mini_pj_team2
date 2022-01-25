from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Comment, Board_title, User

#############실제 구현에 필요없는 기능#################
# 임시: 모든 댓글 확인용
def view_comment(request):
    comment_list = Comment.objects.all()
    temp_out = ''
    for i in comment_list:
        temp_out += i.comment + "<br>"
    return HttpResponse(temp_out)
# 임시: 테스트로 입력한 데이터를 DB에서 삭제
def delete_comment(request):
    data = Comment.objects.filter(comment = "두둥탁두둥탁")
    data.delete()
    return HttpResponse("데이터 삭제 완료")
#######################################################


# 현재 로그인한 회원만 입력가능
# 댓글 작성 양식
def make_comment(request):
    #임시로 로그인 한 척
    request.session['u_id_col'] = 'user4'
    # if user.is_authenticated: # 장고 기본기능이면 이걸 가져와야할 듯
    if request.method == 'POST':
        if request.POST.get('input_comment'):

            board_id = 1 # 게시판 번호는 해당 게시글 url에서 가져올 수 있도록 해야함
            title_id = Board_title.objects.filter(t_num = 1)[0] # 마찬가지로 url에서 가져와야함
            user_id = User.objects.get(u_id = request.session['u_id_col']) #로그인 상태의 유저 아이디를 가져옴
            comment_txt = request.POST.get('input_comment')
            
            one_comment = Comment(
                b_id = board_id,
                board_title = title_id,
                u_id_col = user_id,
                comment = comment_txt)
            one_comment.save()
            return redirect('../../comment/make_comment/')

    comment_list = Comment.objects.all()
    return render(
        request, 
        'make_comment_app/comment_box.html',
        {'comment_list': comment_list})


# Create your views here.

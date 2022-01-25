from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Comment

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
    data = Comment.objects.filter(c_id = 56)
    data.delete()
    return HttpResponse("데이터 삭제 완료")
#######################################################


# 현재 로그인한 회원만 입력가능
# 댓글 작성 양식
def make_comment(request):
    #임시로 로그인 한 척
    request.session['u_id'] = 'user4'
    # if user.is_authenticated: # 장고 기본기능이면 이걸 가져와야할 듯
    if request.method == 'POST':
        if request.POST.get('input_comment'):
            board_id = 1 # 게시판 번호는 해당 게시글 url에서 가져올 수 있도록 해야함
            title_id = 30 # 마찬가지로 url에서 가져와야함
            user_id = request.session['u_id']
            comment_txt = request.POST.get('input_comment')

            one_comment = Comment(
                b_id = board_id,
                t_num = title_id,
                u_id = user_id,
                comment = comment_txt)
            one_comment.save()
            return HttpResponse("댓글 작성 완료") # 작성 완료되면 다시 게시글을 조회하는 형태로 작성 필요

    return render(request, 'make_comment_app/comment_box.html')


# Create your views here.

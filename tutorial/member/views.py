from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

# user 출력
def user(request):
   user_list = User.objects.all()
   return render(
        request,
        'member/line.html',
        {'user_list': user_list }
   )

from .models import User
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

        u = User(
            u_id=user_id, pw=user_pw, u_name=user_name, 
            birth_date=birth_date, nickname=nickname, phone_num=phone_num, email=email)
        u.date_joined = timezone.now()
        u.save()
        return HttpResponse(
            '가입 완료<br>%s %s %s' % (user_id, user_pw, user_name))
    else:
        return render(request, 'member/signup_custom.html')

#로그인
def login_custom(request):
    user_list = User.objects.all()
    if request.method == 'POST':
        user_id = request.POST.get('u_id')
        user_pw = request.POST.get('pw')
        try:
            u = User.objects.get(u_id=user_id, pw=user_pw)
            # 회원정보 조회 실패 시 예외 발생
        except:
            return HttpResponse('로그인 실패')
        else: #로그인 판단 요소 ==> 나중에 이걸로 다양한 정보 확인(동현에이블러님 활용)
            request.session['u_id'] = u.u_id
            request.session['u_name'] = u.u_name
        return render(
        request,
        'member/login_custom.html',
        {'user_list': user_list }
    )   
      
    else:
        return render(request, 'member/login_custom.html')

#로그아웃
def logout_custom(request):
    del request.session['u_id'] # 개별 삭제
    del request.session['u_name'] # 개별 삭제
    request.session.flush() # 전체 삭제
    return redirect('member:login_custom')

##이거 안씀
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('u_name')
            raw_password = form.cleaned_data.get('pw')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('member:login')
    else:
        form = UserForm()
    return render(request, 'member/signup.html', {'form': form})


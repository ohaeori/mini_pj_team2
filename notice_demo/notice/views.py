from multiprocessing.spawn import import_main_path
from django.shortcuts import redirect, render
from matplotlib.pyplot import title
from .models import Notice
from django.http import HttpResponse
from .forms import UploadFileForm,UploadFile

# Create your views here.
#처음화면
def index(request):
    return render(request,'notice/index.html')

#게시글 목록 표시
def notice_list(request): 
    notice_list=Notice.objects.all()
    return render(request, 'notice/notice_list.html',{'notice_list':notice_list})

#게시글 작성
def create_notice(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploadFile = form.save()
            # uploadFile = form.save(commit=False)
            name = uploadFile.file.name
            size = uploadFile.file.size
        if request.POST.get('file',False):
            new_article=Notice.objects.create(
                title=request.POST['title'],
                contents=request.POST['contents'],
                photo=request.POST.get('file',False),
            )
        else:
            new_article=Notice.objects.create(
                title=request.POST['title'],
                contents=request.POST['contents'],
                photo=request.POST.get('file',False),
            )
        return redirect('/notice_list/')
    return render(request, 'notice/create_notice.html')

#게시글 등록
def posting(request,pk):
    poster=Notice.objects.get(pk=pk)
    id = request.GET.get('pk')
    uploadFile = UploadFile.objects.get(id=pk)
    return render(request,'notice/posting.html',{'poster':poster, 'uploadFile':uploadFile})


def upload1(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploadFile = form.save()
            # uploadFile = form.save(commit=False)
            name = uploadFile.file.name
            size = uploadFile.file.size
            #return HttpResponse('%s<br>%s' % (name, size))
    else:
        form = UploadFileForm()
    return render(
        request, 'notice/upload1.html', {'form': form})
#게시글 삭제
def delete_notice(request, pk):
    poster = Notice.objects.get(pk=pk)
    if request.method == 'POST':
        poster.delete()
        return redirect('/notice_list/')
    return render(request, 'notice/delete_notice.html', {'poster': poster})

def img_show(request):
    id = request.GET.get('id')
    uploadFile = UploadFile.objects.get(id=id)
    return render( request, 'notice/img_show.html', {'uploadFile': uploadFile})
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse('<u>home</u>')

def text(request, char):
    return HttpResponse(char)

def date(request, year, month):
    return HttpResponse('%s - %s' %(year, month))

def search(request):
    title = request.GET.get('title')
    return HttpResponse('search:%s'%(title))

def info(request):
    id = request.GET.get('id')
    return HttpResponse('id:%s'%(id))
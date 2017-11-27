# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
from linkstart.models import Index
from django.http import HttpRequest,HttpResponseNotFound,Http404

# Create your views here.
def index(request):
    Content_0 = Index.objects.filter(title='otherworld.link')
    Content_1 = Index.objects.filter(title='创建个人领域')
    Content_2 = Index.objects.filter(title='进入连接点')
    list_1 = [1,2,3,4,5]
    html = '<h1>我是html</h1>'
    return render(request,'index.html',
                  {'p0':Content_0,
                   'p1':Content_1,
                   'p2':Content_2,
                   'list_1':list_1,
                   'html':html})
def linkstart(request):
    return render(request,'linkstart.html',{
                                            'username':'暗夜男',
                                            'userid':'UID00001',
                                            'linkto_num':96,
                                            'linkwith_num':45,
                                            'publish_time':'23:23',
    })
def linkhub(request):
    return render(request,'linkhub.html')
def homeworld(request,id):
    return render(request,'homeworld.html')
def temp(request):
    a = request.META
    # return HttpResponseNotFound('<h1>页面丢失了</h1>')
    # return render(request, 'base.html')
    # try:
    #     Content_0 = Index.objects.filter(title='otherworld.link')
    # except Poll.DoesNotExist:
    return render(request,'base.html')
def new_temp(request):
    return render(request,'new_temp.html')
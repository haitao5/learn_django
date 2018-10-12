from django.http import HttpResponse
from django.shortcuts import render

def hello1(request):
    # django.http.HttpResponse() 来输出 "Hello World！"。
    # 该方式将数据与视图混合在一起，不符合 Django 的 MVC 思想
    return HttpResponse("Hello world 1 ! ")

def hello2(request):
    #  Django 模板的应用，模板是一个文本，用于分离文档的表现形式和内容
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

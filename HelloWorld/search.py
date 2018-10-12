# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render_to_response
 

"""
使用了GET方法。视图显示和请求处理分成两个函数处理

HTTP协议以"请求－回复"的方式工作。
客户发送请求时，可以在请求中附加数据。
服务器通过解析请求，就可以获得客户传来的数据，并根据URL来提供特定的服务。
"""


# 表单
def search_form(request):
    # 显示搜索界面
    # 使用render_to_response方法调用html模板
    return render_to_response('search_form.html')
 
# 接收请求数据
def search(request):  
    # 返回搜索结果
    # 使用HttpResponse直接反馈信息
    request.encoding='utf-8'
    
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
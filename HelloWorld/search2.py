# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.views.decorators import csrf
 

"""
POST方法并用一个URL和处理函数，同时显示视图和处理请求
"""


# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.method == 'GET':
        ctx['rlt'] = '请提交'
        ctx['user'] = ''
    elif request.method == 'POST':    
        ctx['rlt'] = '输入结果： ' + request.POST['q']
        ctx['user'] = 'User: ' + str(request.META['USERNAME'])
    else:
        ctx['rlt'] = '' 
        ctx['user'] = ''
    return render(request, "post.html", ctx)
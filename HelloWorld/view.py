from django.http import HttpResponse
from django.shortcuts import render
 
def hello1(request):
    return HttpResponse("Hello world 1 ! ")

def hello2(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

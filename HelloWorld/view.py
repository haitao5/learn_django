from django.http import HttpResponse
 
def hello1(request):
    return HttpResponse("Hello world 1 ! ")

def hello2(request):
    return HttpResponse("Hello world 2! ")

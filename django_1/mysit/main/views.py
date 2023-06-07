from django.shortcuts import render, HttpResponse

# Create your views here.
def mainpage(request):
    return HttpResponse('hello wtytytytytytytyorld')


def about(request):
    return HttpResponse('about')
    

def yuko(request):
    return HttpResponse('yuko')
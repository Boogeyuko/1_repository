from django.shortcuts import render, HttpResponse

def page(request):
    return HttpResponse('hello people')

# Create your views here.

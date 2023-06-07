from django.shortcuts import render, HttpResponse
from .models import mainpage


def homepage(request):
    main = mainpage.objects.last()
    context = {
        'main': main,
    }
    return render(request, 'yuko/main.html', context)


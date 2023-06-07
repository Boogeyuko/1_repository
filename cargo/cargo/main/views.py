from django.shortcuts import HttpResponse, render



def homepage(request):
    
    context = {
        'main': "____",
    }
    return render(request,'main/index.html', context)



# Create your views here.

from django.shortcuts import render



def home_view(request):
    
    return render(request,'page/index.html')


def adaklik_view(request):

    return render(request,"page/adaklik.html")

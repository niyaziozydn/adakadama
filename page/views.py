from django.shortcuts import render,redirect




def home_view(request):
    
    
    return render(request,'page/index.html')


def adaklik_view(request):

    return render(request,"page/adaklik.html")


def urunlerimiz_view(request):

    return render(request,'page/urunlerimiz.html')




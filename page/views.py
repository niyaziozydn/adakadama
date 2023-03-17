from django.shortcuts import render,redirect
from .models import Post




def home_view(request):
    
    
    return render(request,'page/index.html')


def adaklik_view(request):

    return render(request,"page/adaklik.html")


def urunlerimiz_view(request):

    return render(request,'page/urunlerimiz.html')



def post_view(request):
    posts = Post.objects.all().order_by('-created_on')
    context = dict(
        posts=posts
    )
    return render(request,"page/post.html",context)
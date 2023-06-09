from django.shortcuts import render,redirect
from .models import Post
from django.core.paginator import Paginator





def home_view(request):
    
    
    return render(request,'page/index.html')


def adaklik_view(request):

    return render(request,"page/adaklik.html")


def urunlerimiz_view(request):

    return render(request,'page/urunlerimiz.html')



def post_view(request):
    posts = Post.objects.all().order_by('-created_on')
    page_num = request.GET.get('page_num')
    post_paginator = Paginator(posts,6)

    context = dict(
        posts=post_paginator.get_page(page_num),
    )
    return render(request,"page/post.html",context)
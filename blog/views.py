from django.shortcuts import render
from .models import *



def HomeView(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    
    return render(request, 'blog/home.html', context)
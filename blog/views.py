from django.shortcuts import render, redirect
from .models import *
from .forms import *




def HomeView(request):
    posts = Post.objects.all().order_by('-date_created')
    context = {
        'posts': posts
    }
    
    return render(request, 'blog/home.html', context)





def NewPost(request):
        
    form = PostForm()
    if request.method == 'POST':
    #print('Printing POST:', request.POST)    
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}

    return render(request, 'blog/newpost.html', context)


def PostDetail(request, pk):
    post = Post.objects.get(id=pk)

    context = {
        'post': post,
    }

    return render(request, 'blog/postDetail.html', context)
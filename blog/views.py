from django.shortcuts import render

from .models import Post

def show_posts(request):   
    posts = Post.objects.order_by('-posted')[0:3]
    return render(request, 'blog/blog.html', {'posts': posts})

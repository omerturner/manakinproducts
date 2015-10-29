from django.shortcuts import render

from .models import Post
from products.models import Product


def show_posts(request):   
    posts = Post.objects.order_by('-posted')[0:3]
    product = Product.objects.all()[0]
    return render(request, 'blog/blog.html', {'posts': posts, 'product': product})

from django.shortcuts import render

from .models import Blog

def blogs(request):
    blogs=Blog.objects.order_by('-id').all()
    context={
        'blogs':blogs
    }
    return render(request,'blog/blogs.html',context)

def blog(request,id):
    blog=Blog.objects.get(id=id)
    context={
        'blog':blog
    }
    return render(request,'blog/blog-details.html',context)

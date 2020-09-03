from django.shortcuts import render,get_object_or_404
from django.http import  HttpResponse
from . import models

# Create your views here.
def blog(request):

    all_blogs=models.blog.objects.order_by('-date')[:5]
    return render(request,"blog/blog.html",{"all_blogs":all_blogs})


def all_blogs(request):
    all_blogs=models.blog.objects.order_by('-date')[5:]
    return render(request,"blog/all_blogs.html",{"all_blogs":all_blogs})

def detail(request,blog_id):
    blog=get_object_or_404(models.blog,pk=blog_id)
    return render(request,"blog/detail.html",{"blog_id":blog})

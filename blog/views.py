from django.shortcuts import render, HttpResponse
from blog.models import Post


# Create your views here.
def index(request):
    post_latest = Post.objects.order_by("-createDate")[:5]
    context = {
        "post_latest": post_latest
        
        
    }
    return render(request,"index.html",context=context)

def about(request):
    context = {
        
        
    }
    return render(request,"about.html",context=context)

def contact(request):
    context = {
        
        
    }
    return render(request,"contact.html",context=context)

def post(request):
    post_latest = Post.objects.order_by("-createDate")[:5]
    context = {
        "post_latest": post_latest
        
        
    }
    return render(request,"post.html",context=context)
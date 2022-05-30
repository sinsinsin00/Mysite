from django.shortcuts import render, HttpResponse
from blog.models import Post
from django.views import generic


# Create your views here.
def index(request):
    post_latest = Post.objects.order_by("-createDate")[:3]
    context = {"post_latest": post_latest}
    return render(request, "index.html", context=context)

def about(request):
    context = {}
    return render(request, "about.html", context=context)

def contact(request):
    context = {}
    return render(request, "contact.html", context=context)

def postlist(request):
    post_latest = Post.objects.order_by("-createDate")
    context = {"post_latest": post_latest}
    return render(request, "postlist.html", context=context)

class PostDetailView(generic.DetailView):
    model = Post

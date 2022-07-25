from django.shortcuts import render, HttpResponse
from blog.models import Post
from django.views import generic


# Create your views here.
def index(request):
    post_latest = Post.objects.order_by("-createDate")[:3]
    context = {"post_latest": post_latest}
    return render(request, "index.html", context=context)

def about(request):
    post_latest = Post.objects.order_by("-createDate")
    context = {"post_latest": post_latest}
    return render(request, "about.html", context=context)

def projects(request):
    context = {}
    return render(request, "projects.html", context=context)

def skills(request):
    context = {}
    return render(request, "skills.html", context=context)

class PostDetailView(generic.DetailView):
    model = Post

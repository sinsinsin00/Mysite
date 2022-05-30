from django.shortcuts import render, HttpResponse
from django.views import generic


# Create your views here.
def shinstagram(request):
    context = {}
    return render(request, "shinstagram.html", context=context)

from django.shortcuts import render, render
from rest_framework.views import APIView
from content.models import Feed


# Create your views here.
class Main(APIView):
    def shinstagram(request):
        feed_list = Feed.objects.all().order_by('-id')
        return render(request, "shinstagram.html", context=dict(feed_list=feed_list))

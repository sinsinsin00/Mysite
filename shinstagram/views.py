from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from content.models import Feed
import os
from mysite.settings import MEDIA_ROOT
from uuid import uuid4

# Create your views here.
class Main(APIView):
    def shinstagram(request):
        feed_list = Feed.objects.all().order_by('-id')
        return render(request, "shinstagram.html", context=dict(feed_list=feed_list))

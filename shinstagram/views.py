from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from content.models import Feed
from user.models import User
import os
from mysite.settings import MEDIA_ROOT
from uuid import uuid4

# Create your views here.
class Main(APIView):
    def shinstagram(request):
        feed_list = Feed.objects.all().order_by('-id')
        
        email = request.session.get('email', None)
        
        if email is None:
            return render(request, "login.html")  
        
        user = User.objects.filter(email=email).first()
        
        if user is None:
            return render(request, "login.html")  
        

        return render(request, "shinstagram.html", context=dict(feed_list=feed_list, user=user))
 

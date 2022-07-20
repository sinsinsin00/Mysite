from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from content.models import Feed, Reply, Like, BookMark
import os
from mysite.settings import MEDIA_ROOT
from uuid import uuid4

# Create your views here.
class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        content = request.data.get('content')
        image = uuid_name
        email = request.data.get('email')


        Feed.objects.create(content=content, image=image, email=email)

        return Response(status=200)
    
class UploadReply(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        reply_content = request.data.get('reply_content', None)
        email = request.session.get('email', None)
        
        Reply.objects.create(feed_id=feed_id, reply_content=reply_content, email=email)
        
        return Response(status=200)
    
    
class TogleLike(APIView):
    def post(self, request):
        feed_id         = request.data.get('feed_id', None)
        is_like         = request.data.get('favorite_status', None) 
        email           = request.session.get('email', None) 
        userLike        = Like.objects.filter(feed_id=feed_id, email=email).first()

        if userLike:
            userLike.is_like = is_like
            userLike.save()
          
        else:   
            Like.objects.create(feed_id=feed_id, email=email, is_like=is_like) 
        
        return Response(status=200)
        
    
class TogleBookMark(APIView):
    def post(self, request):
        feed_id         = request.data.get('feed_id', None)
        is_marked       = request.data.get('bookmark_status', None) 
        email           = request.session.get('email', None) 
        userBook        = BookMark.objects.filter(feed_id=feed_id, email=email).first()
        
        if userBook:
            userBook.is_marked = is_marked
            userBook.save()
          
        else:   
            BookMark.objects.create(feed_id=feed_id, email=email, is_marked=is_marked)
            
        
        return Response(status=200)
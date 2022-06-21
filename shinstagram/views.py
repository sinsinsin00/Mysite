from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from content.models import Feed, Reply, Like, BookMark
from user.models import User
import os
from mysite.settings import MEDIA_ROOT
from uuid import uuid4

# Create your views here.
class Main(APIView):
    def shinstagram(request):
        email = request.session.get('email', None)      #접속 상태 여부 확인 
        if email is None:
            return render(request, "login.html")  
        user = User.objects.filter(email=email).first()
        user_id = user.email[0:user.email.find('@')]
        feed_list = []
        object_feed_list = Feed.objects.all().order_by('-id')
        
        
        for feed in object_feed_list:
            try:
                feed_user = User.objects.filter(email=feed.email).first()
                feed_user_id = feed_user.email[0:feed_user.email.find('@')]
                feed_user_profile_image = feed_user.profile_image
                feed_like = Like.objects.filter(feed_id=feed.id, email=email, is_like=True).exists()
                feed_book = BookMark.objects.filter(feed_id=feed.id, email=email, is_marked=True).exists()
                reply_object_list = Reply.objects.filter(feed_id=feed.id)
                reply_list = []
                
                for reply in reply_object_list:
                    reply_user_id = reply.email[0:reply.email.find('@')]
                    reply_list.append(dict(reply_content=reply.reply_content, 
                                           reply_user_id=reply_user_id, 
                                           
                                           ))
                
                reply_count = len(reply_list)
                feed_list.append(dict(feed_id=feed.id,
                                    image=feed.image,
                                    content=feed.content,
                                    is_liked=feed_like,
                                    is_booked=feed_book,
                                    feed_user_profile_image=feed_user_profile_image,
                                    feed_user_id=feed_user_id,
                                    reply_list=reply_list,
                                    reply_count=reply_count,
                                    
                                    ))
            except Exception as e:
                print(e)
        
        return render(request, "shinstagram.html", context=dict(feed_list=feed_list, 
                                                                user_id=user_id, 
                                                                user=user, 
                                                                reply_user_id=reply_user_id,
                                                                
                                                                ))
 
class Profile(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()
        #user_content_list = Feed.objects.all()
        user_id = user.email[0:user.email.find('@')]
        
        
        
        return render(request, "profile.html", context=dict(#user_content_list=user_content_list, 
                                                             user_id=user_id, 
                                                             user=user,
                                                            ))
    
    def post(self, request):
        pass
    
class UploadProfile(APIView):
    def get(self, request):
        pass
    
    def post(self, request):
        file = request.FILES['file']
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()

        if user.profile_image != 'default_image.jpg':
            try:
                print("os path : ",os.path.join(MEDIA_ROOT,user.profile_image))
                os.remove(os.path.join(MEDIA_ROOT,user.profile_image))    
            except Exception as e:
                print(e)

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        profile_image = uuid_name
        user.profile_image = profile_image
        user.save()
        
        return Response(status=200)
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth         import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
import os
from mysite.settings import MEDIA_ROOT
from uuid import uuid4

# Create your views here.
class Join(APIView):
    def get(self, request):
        return render(request,"join.html")
    
    def post(self, request):
        email = request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)
        
        if User.objects.filter(email=email).exists():
            return Response(status=500, data=dict(message='해당 이메일 주소가 존재합니다'))
        
        
        User.objects.create(email=email, 
                            nickname=nickname, 
                            name=name, 
                            password=make_password(password),
                            profile_image="default_image.jpg")
         
        return Response(status=200, data=dict(message="회원가입 성공했습니다."))
        
    
class Login(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        
        if email is not None:
            return redirect("http://evolabs.co.kr/shinstagram")  
        
        return render(request,"login.html")
    
    def post(self, request):
        email = request.data.get('email', None)         
        password = request.data.get('password', None)
        
        if email is not None:
            user = User.objects.filter(email=email).first()
        else:
            return Response(status=400, data=dict(message="이메일을 입력해주세요"))
        
        if password is None:
            return Response(status=400, data=dict(message='비밀번호를 입력해주세요'))
        
        if user is None:
            return Response(status=400, data=dict(message='입력 정보가 잘못되었습니다'))
            
        if check_password(password, user.password) is False:
            return Response(status=400, data=dict(message='입력 정보가 잘못되었습니다'))
            
        request.session['loginCheck'] = True
        request.session['email'] = user.email
        
        return Response(status=200, data=dict(message='로그인에 성공하였습니다'))
    
class Logout(APIView):
    def get(self, request):
            request.session.flush()
            return render(request,"login.html")
    
    def post(self, request):
        pass
    

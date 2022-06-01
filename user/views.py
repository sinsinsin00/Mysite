from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User

# Create your views here.
class Join(APIView):
    def get(request):
        return render(request,"join.html")
    
    def post(request):
        email = request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)
        
        User.objects.create(email=email, 
                            nickname=nickname, 
                            name=name, 
                            password=make_password(password)
                            profile_image="default_image.jpg"
                            )
        return Response(status=200)
        
    
class Login(APIView):
    def get(request):
        return render(request,"login.html")
    
    def post(requst):
        pass            
            
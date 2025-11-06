from django.shortcuts import render
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt import authentication
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView,status
from django.contrib.auth.models import User
from models_manager.models import UserProfile 
from django.contrib.auth import authenticate
from .Serializer import signupSerializer
# Create your views here.
"----------------------------user login / Signup Handlear section--------------------------------------------------------------------------------------------------------------------"
class UserSignupHandler(APIView): 
    authentication_classes=[]
    permission_classes=[AllowAny]
    def post(self,request): #signup
            serializers=signupSerializer(data=request.data)
            if serializers.is_valid():
                new_user=serializers.save()
                token=RefreshToken.for_user(new_user)
                print(new_user)
                return Response({'message':"user created sucessfully"},status=status.HTTP_200_OK)
            else:
                return Response({"message":"inavlid data"},status=status.HTTP_400_BAD_REQUEST)
        
class UserLoginHandler(APIView):
    authentication_classes=[]
    permission_classes=[AllowAny]
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        if username and password:
            user=User.objects.filter(username=username)
            user=authenticate(username=username,password=password)
            if user is not None:
                token=RefreshToken.for_user(user)
                return Response({'message':"user logged in sucessfully","token":str(token.access_token)},status=status.HTTP_200_OK)
            else:
                return Response({"message":"user not found"},status=status.HTTP_400_BAD_REQUEST)    
            
        else:
            return Response({",message":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
    
"-------------------------------------------------------X----------------------------------------------------------------------------------------------"    

"--------------------user profile handler----------------------------------------------------------------------------------------------------------------"
class UserProfile(APIView):
    
   
    def get(self,request):
        user=request.user
        user_profile=UserProfile.objects.get(user=user)
        if user_profile:
            return Response({"message":"user profile found","user_profile":user_profile},status=status.HTTP_200_ok)
        

    def put(self,request):
        user=request.user
        user_profile=UserProfileSerializer(data=request.data)
        if user_profile.is_valid():
            user_profile.save(user=user)
            return Response({"message":"user profile updated"},status=status.HTTP_200_OK)
        else:
            return Response({"message":"invalid data"},status=status.HTTP_400_BAD_REQUEST)

"-------------------------------------------------X-----------------------------------------------------------------------------------------------------"
"-----------------------------------------Admin Handlear------------------------------------------------------------------------------------------------------------------"
class AdminCreater(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        if username and password:
            User.objects.create_superuser(username=username,password=password)
            return Response({"message":"admin created sucessfully"},status=status.HTTP_200_OK)  
        
        else:
            return Response({"message":"invalid data"},status=status.HTTP_400_BAD_REQUES)
"-------------------------------------------X-------------------------------------------------------------------------------------------------------------------"

"-------------------------------------------Get UserList-------------------------------------------------------------------------------------------------------------------"
class UserList(APIView):
   
    def get(self,request):
        users=User.objects.all()
        serializer=UserProfileSerializer(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
"--------------------------------------------X------------------------------------------------------------------------------------------------------------------------------"
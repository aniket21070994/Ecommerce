from django.shortcuts import render
from rest_framework import response,authentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView,status
from django.contrib.auth.models import User
from models_manager.models import UserProfile
from .Serializer import UserProfileSerializer
# Create your views here.
"----------------------------user login / Signup Handlear section--------------------------------------------------------------------------------------------------------------------"
class UserSignupHandler(APIView): 
    
    def post(self,request): #signup
        username=request.data.get('username')
        password=request.data.get('password')
        if username and password:
            new_user=User.objects.create_user(password=password,username=username)
            token=RefreshToken.for_user(new_user)
            return response({'message':"user created sucessfully"},status=status.HTTP_200_OK)
        else:
            return response({"message":"inavlid data"},status=status.HTTP_400_BAD_REQUEST)
        
class UserLoginHandler(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        if username and password:
            user=User.objects.filter(username=username).first()
            if user is not None:
                token=RefreshToken.for_user(user)
                return response({'message':"user logged in sucessfully","token":str(token.access_token)},status=status.HTTP_200_OK)
            else:
                return response({"message":"user not found"},status=status.HTTP_400_BAD_REQUEST)    
            
        else:
            return response({",message":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
    
"-------------------------------------------------------X----------------------------------------------------------------------------------------------"    

"--------------------user profile handler----------------------------------------------------------------------------------------------------------------"
class UserProfile(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    def get(self,request):
        user=request.user
        user_profile=UserProfile.objects.get(user=user)
        if user_profile:
            return response({"message":"user profile found","user_profile":user_profile},status=status.HTTP_200_ok)
        

    def put(self,request):
        user=request.user
        user_profile=UserProfileSerializer(data=request.data)
        if user_profile.is_valid():
            user_profile.save(user=user)
            return response({"message":"user profile updated"},status=status.HTTP_200_OK)
        else:
            return response({"message":"invalid data"},status=status.HTTP_400_BAD_REQUEST)

"-------------------------------------------------X-----------------------------------------------------------------------------------------------------"
"-----------------------------------------Admin Handlear------------------------------------------------------------------------------------------------------------------"
class AdminCreater(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        if username and password:
            User.objects.create_superuser(username=username,password=password)
            return response({"message":"admin created sucessfully"},status=status.HTTP_200_OK)  
        
        else:
            return response({"message":"invalid data"},status=status.HTTP_400_BAD_REQUES)
"-------------------------------------------X-------------------------------------------------------------------------------------------------------------------"

"-------------------------------------------Get UserList-------------------------------------------------------------------------------------------------------------------"
class UserList(APIView):
    def get(self,request):
        users=User.objects.all()
        serializer=UserProfileSerializer(users,many=True)
        return response(serializer.data,status=status.HTTP_200_OK)
"--------------------------------------------X------------------------------------------------------------------------------------------------------------------------------"
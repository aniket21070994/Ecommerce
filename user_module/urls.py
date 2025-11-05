
from django.urls import path
from . views import UserSignupHandler,UserLoginHandler,UserProfile,AdminCreater,UserList

from . import admin
urlpatterns = [
 path('register/',UserSignupHandler.as_view(),name='register'),
 path('login/',UserLoginHandler.as_view(),name='login'),
 path('profile/',UserProfile.as_view(),name='profile'),
 path('create-admin/',AdminCreater.as_view(),name='admin'),
 path('users/',UserList.as_view(),name='user')
]

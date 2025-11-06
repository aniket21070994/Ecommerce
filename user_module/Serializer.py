from rest_framework import serializers
from models_manager.models import UserProfile
from django.contrib.auth.models import User

class signupSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    email=serializers.EmailField()
    first_name=serializers.CharField()
    phone_number=serializers.CharField()
    role=serializers.CharField()
    def validate(self, values):
        username=values.get('username')
        if User.objects.filter(username=username):
            return ValueError("User alredy exists")
        return values 

    def create(self, validated_data):
        role=validated_data.pop('role')
        phone_number=validated_data.pop('phone_number')
        user=User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user,role=role,phone_number=phone_number)
        return user
       
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields='__all__'
        
from rest_framework import serializers
from models_manager.models import UserProfile
from django.contrib.auth.models import User
from django.db import transaction

'''
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [ 'phone_number', 'date_of_birth', 'gender', 'profile_image', 'default_address', 'role']

'''

class signupSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    name = serializers.CharField()
    phone_number = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    date_of_birth = serializers.DateField(required=False, allow_null=True)
    gender = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    profile_image = serializers.ImageField(required=False, allow_null=True)
    default_address = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    role = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def validate(self, values):
        username = values.get('username')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("user already exist")
        return values

    @transaction.atomic
    def create(self, validated_data):
        password = validated_data.pop('password')
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        name = validated_data.pop('name')
        user = User.objects.create_user(username=username, password=password, email=email, first_name=name)
        # Create UserProfile with the remaining validated_data
        UserProfile.objects.create(user=user, **validated_data)
        return user
       


    


    
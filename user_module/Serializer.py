from rest_framework import serializers
from models_manager.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [ 'phone_number', 'date_of_birth', 'gender', 'profile_image', 'default_address', 'role']


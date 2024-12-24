from rest_framework import serializers
from django.contrib.auth.models import User

from user_management.models import TodoUserProfile


class TodoUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoUserProfile
        fields = ('phone_number','lucky_number')

class UserSerializer(serializers.ModelSerializer):

    profile = TodoUserProfileSerializer(source='todouserprofile')

    class Meta:
        model = User
        fields = ('id', 'username' ,'last_name' ,'first_name' ,'email','profile')

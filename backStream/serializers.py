from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Streams, News

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 
    # userdetail = UserDetailSerializer(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name','is_staff', 'is_active', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        
        
class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model= Streams
        fields= "__all__"
        
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model= News
        fields= "__all__"

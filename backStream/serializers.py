from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Streams, News

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= "__all__"
        
        
class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model= Streams
        fields= "__all__"
        
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model= News
        fields= "__all__"

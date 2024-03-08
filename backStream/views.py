from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import *
from .models import *
# Create your views here.


class UserViews(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class StreamViewset(viewsets.ModelViewSet):
    queryset = Streams.objects.all()
    serializer_class= StreamSerializer
    
class NewsViewset(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
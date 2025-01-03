from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() 
    #this is a list of already created users so that we don't have to create a new use rif the user exist
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
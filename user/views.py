from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.hashers import make_password

from .serializers import CustomUserSerializer
from .models import CustomUser

#to check if jwt is working with a account
class HelloView(APIView):
    permission_classes = (IsAuthenticated, ) #as long as this class is present we'll have to authenticate the user
  
    def get(self,request):
        content = {'message': 'Congratulations on setting up your first JWT authenticated django project!'}
        user = request.user
        serializer = CustomUserSerializer(user, many = False)
        return Response({
                "user": serializer.data,
                "message": content
                }, status=status.HTTP_201_CREATED)
    
    
#to create a new user and get all users
class User(APIView):
    def post(self,request):
        data = request.data
        user_serializer = CustomUserSerializer(data = data)

        password = request.data['password']
        password = make_password(password=password) #it is used to hash the incoming password

        #if valid then make the user and assign a token
        if user_serializer.is_valid():
            user  = user_serializer.save(password=password)

        #else raise an error 
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #return the response

        return Response({
            "user": user_serializer.data,
            "message":"user created successfully!"
        }, status=status.HTTP_201_CREATED)
    
    def get(self,request):
        user = CustomUser.objects.all()
        serializer = CustomUserSerializer(user, many = True)
        return Response(serializer.data)
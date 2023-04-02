from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import CustomUserSerializer
from .models import CustomUser


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
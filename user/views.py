from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HelloView(APIView):
    permission_classes = (IsAuthenticated, ) #as long as this class is present we'll have to authenticate the user
  
    def get(self, request):
        content = {'message': 'Congratulations on setting up your first JWT authenticated django project!'}
        return Response(content)
#import model serializer

from rest_framework.serializers import ModelSerializer

from .models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email','name','password']
        extra_kwargs = {'password': {'write_only': True}}
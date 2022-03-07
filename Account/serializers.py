from dataclasses import fields
from rest_framework import serializers
from .models import User,Book


class RegistrationSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(max_length=255,min_length=6,write_only=True) 
    
    class Meta:
        model=User
        fields=['first_name','last_name','user_name','email','password','is_staff','is_admin']
        
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)    
    
    
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book 
        fields=['name','author']   
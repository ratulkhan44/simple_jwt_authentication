from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from django.conf import settings
from .serializers import RegistrationSerializer,BookSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from rest_framework.permissions import IsAuthenticated
import json
# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            request = self.context["request"]
            if 'email' in request.data and 'password' in request.data:
                email = request.data.get('email',None)
                password = request.data.get('password',None)
                print("=============yesss================",email,password)
                
        except KeyError:
            pass
        data=super().validate(attrs)
        token=self.get_token(self.user)
        data['refresh']=str(token)
        data['access']=str(token.access_token)
        data['type']='Bearer'
        data['name']=self.user.user_name
        data['is_superuser'] = self.user.is_superuser
        data['is_staff'] = self.user.is_staff
        data['lifetime']=settings.SIMPLE_JWT.get('ACCESS_TOKEN_LIFETIME',0)
        return data
    
    
class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    
class RegistrationApiView(APIView):
    def post(self,request,format=None):
        serializer=RegistrationSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            obj=serializer.save()
        
        return Response(serializer.data)    
    
    
class BookListView(APIView):
    permission_classes= [IsAuthenticated]
    
    def post(self,request,format=None):
        serializer= BookSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            obj=serializer.save()
        
        return Response(serializer.data)
    
    
    def get(self,request):
        queryset=Book.objects.all()
        serializer = BookSerializer(queryset,many=True)
        return Response(serializer.data)
        
        
        

from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from django.conf import settings
from .serializers import RegistrationSerializer,BookSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data=super().validate(attrs)
        refresh=self.get_token(self.user)
        data['refresh']=str(refresh)
        data['access']=str(refresh.access_token)
        data['type']='Bearer'
        data['lifetime']=settings.SIMPLE_JWT.get('ACCESS_TOKEN_LIFETIME',0)
        return data
    
    
class MyTokenObtainPairView(TokenObtainPairView):
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
        
        
        

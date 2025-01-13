from django.shortcuts import render
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer, TokenSerializer
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Social Media API!!")

# Create your views here.
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.create(user=user)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request}) 
        serializer.is_valid(raise_exception=True) 
        user = serializer.validated_data['user'] 
        token, created = Token.objects.get_or_create(user=user) 
        return Response({'token': token.key, 'user_id': user.id, 'email': user.email})
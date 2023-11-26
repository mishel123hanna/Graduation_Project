from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render
from djoser.views import UserViewSet
from .serializers import UserCreateSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from rest_framework.permissions import AllowAny

from rest_framework.decorators import api_view, permission_classes

# Create your views here.

# class CustomUserCreateView(UserViewSet):
#     serializer_class = UserCreateSerializer
   
#     def get(self, request):
#         pass
#     def create(self, request):
#         pass
#     def perform_create(self, serializer):
#         user = serializer.save()
#         return user
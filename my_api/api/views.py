from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
# Create your views here.


class UserApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

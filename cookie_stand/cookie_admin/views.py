from django.shortcuts import render
from rest_framework import generics
from .models import Cookie
from.serializers import CookieSerializer

# CR views
class CookieList(generics.ListCreateAPIView) :

    queryset = Cookie.objects.all()
    serializer_class = CookieSerializer

# RUD view
class CookieDetail(generics.RetrieveUpdateDestroyAPIView) :

    queryset = Cookie.objects.all()
    serializer_class = CookieSerializer

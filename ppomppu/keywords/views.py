from django.shortcuts import render
from rest_framework import generics
from .models import Keywords
from .serializers import KeywordSerializer

class KeywordListView(generics.ListCreateAPIView):
    queryset = Keywords.objects.all()
    serializer_class = KeywordSerializer 

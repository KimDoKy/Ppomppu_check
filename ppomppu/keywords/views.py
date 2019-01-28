from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework import permissions
from .models import Keywords
from .serializers import KeywordSerializer


class KeywordListView(generics.ListCreateAPIView):
    queryset = Keywords.objects.all()
    serializer_class = KeywordSerializer 
    permission_classes = (permissions.IsAuthenticated,)

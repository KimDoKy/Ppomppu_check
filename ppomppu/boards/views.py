from django.shortcuts import render

from rest_framework import generics
from rest_framework import permissions

from .serializers import PostSerializer
from .permissions import IsOwner

from .models import Post

class CreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

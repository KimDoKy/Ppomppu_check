from rest_framework import serializers

from django.conf import settings

from .models import Post

class PostSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field='username', queryset=Post.objects.all())

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'contents', 'create_at', 'update_at', 'photo')
        read_only_fields = ('create_at', 'update_at')

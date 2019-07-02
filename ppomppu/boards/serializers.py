from rest_framework import serializers

from django.conf import settings

from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('__all__')
        read_only_fields = ('create_at', 'update_at')

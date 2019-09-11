from rest_framework import serializers
from .models import CustomUser
from keywords.models import Keywords

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = 'doc_keyword'
        model = Keywords
        fields = ('keyword', 'alarm', 'owner', 'id')

class UserSerializer(serializers.ModelSerializer):
    keywords = KeywordSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'keywords')

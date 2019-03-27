from rest_framework import serializers
from .models import Keywords

class KeywordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keywords
        fields = ('keyword','alarm','update_link', 'id')

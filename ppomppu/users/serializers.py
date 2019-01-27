from rest_framework import serializers
from . import models 
from keywords.serializers import KeywordSerializer as KS

class UserSerializer(serializers.ModelSerializer):
    keywords = KS(many=True)

    class Meta:
        model = models.CustomUser
        fields = ('email', 'username','keywords')

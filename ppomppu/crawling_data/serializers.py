from rest_framework import serializers
from .models import CrawlingData

class CrawlingSerializer(serializers.ModelSerializer):

    class Meta:
        model = CrawlingData
        fields = ('__all__')
        read_only_fields = ('__all__',)

from rest_framework import serializers
from .models import Videos


class VideoSerializer(serializers.ModelSerializer):
    """
    Serializer for Videos
    """
    class Meta:
        model = Videos
        fields = '__all__'

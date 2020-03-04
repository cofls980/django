from rest_framework import serializers
from .models import Text, Color


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ['pid', 'ptext']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['pid', 'pcolor']
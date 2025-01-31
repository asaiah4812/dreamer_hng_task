from rest_framework import serializers
from . models import Dreamer

class DreamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dreamer
        fields = ['email', 'current_datetime', 'github_url']
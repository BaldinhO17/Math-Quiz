from rest_framework import serializers
from Math_Quiz.alternative.models import Alternative

class AlternativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternative
        fields = ['id', 'text', 'isCorrect']
        
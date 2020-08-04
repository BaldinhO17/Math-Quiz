from rest_framework import viewsets
from Math_Quiz.alternative.models import Alternative
from Math_Quiz.alternative.api.serializers import AlternativeSerializer

class AlternativeViewSet(viewsets.ModelViewSet):
    queryset = Alternative.objects.all()
    serializer_class = AlternativeSerializer

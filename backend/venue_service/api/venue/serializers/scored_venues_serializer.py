from rest_framework import serializers  
from .venues_serializer import VenuesSerializer

class ScoredVenuesSerializer(VenuesSerializer):
    score = serializers.FloatField()
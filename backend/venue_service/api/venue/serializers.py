from rest_framework import serializers

class VenuesSerializer(serializers.Serializer):
    name = serializers.StringRelatedField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

class ScoredVenuesSerializer(VenuesSerializer):
    score = serializers.FloatField()
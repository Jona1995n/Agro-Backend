from rest_framework import serializers
from .models import Facility, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['__all__' ]

class FacilitySerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Facility
        fields = ['__all__' ]
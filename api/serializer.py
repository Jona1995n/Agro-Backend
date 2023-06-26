from .models import Facility, Review
from rest_framework import serializers

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ['name', 'category', 'address', 'lat', 'lon']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['title', 'body', 'time']

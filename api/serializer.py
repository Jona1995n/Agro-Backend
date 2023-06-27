from rest_framework import serializers
from .models import Facility, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['title', 
                  'body', 
                  'time', 
                  'stars', 
                  'email', 
                  'user'
                  ]

class FacilitySerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Facility
        fields = ['name', 
                  'category', 
                  'address', 
                  'lat', 
                  'lon',
                  'reviews'
                  ]
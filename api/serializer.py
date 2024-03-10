from rest_framework import serializers
from rest_framework.response import Response
from .models import Facility, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['facility', 'title', 'body', 'time', 'stars', 'email', 'user']

class FacilitySerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    
    class Meta:
        model = Facility
        fields = ['id', 'name', 'category', 'phone_number', 'address', 'email_address', 'lat', 'lon', 'reviews']

    def create(self, validated_data):
        reviews = validated_data.pop('reviews')
        return Facility.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.email_address = validated_data.get('email_address', instance.email_address)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.lon = validated_data.get('lon', instance.lon)
        instance.save()
        return instance
    
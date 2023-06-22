from .models import Facility
from rest_framework import serializers

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ['name', 'category', 'address', 'lat', 'lon']

from rest_framework import viewsets, permissions
from .models import Facility, Review
from .serializer import FacilitySerializer, ReviewSerializer

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permissions = [permissions.IsAuthenticated]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permissions = [permissions.IsAuthenticated]

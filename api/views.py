from .models import Facility
from rest_framework import viewsets, permissions
from .serializer import FacilitySerializer, ReviewSerializer

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permissions = [permissions.IsAuthenticated]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permissions = [permissions.IsAuthenticated]

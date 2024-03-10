from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
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

    def get_queryset(self):
        facility = self.request.query_params.get('facility')
        queryset = Review.objects.filter(facility=facility)
        return queryset

    def get(self, request, *args, **kwargs):
        try:
            facility = request.query_params["facility"]
            if facility != None:
                reviews = Review.objects.get(facility=facility)
                serializer = ReviewSerializer(reviews)
        except:
            reviews = self.get_queryset()
            serializer = ReviewSerializer(reviews, many=True)

        return Response(serializer.data)

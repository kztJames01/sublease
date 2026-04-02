from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import (
    propertyType,
    apartmentListingModel,
    individualListingModel,
    optionalIndividual,
    amenity,
    ListingAmentiy,
)
from .serializers import (
    PropertyTypeSerializer,
    ApartmentListingSerializer,
    IndividualListingSerializer,
    OptionalIndividualSerializer,
    AmenitySerializer,
    ListingAmenitySerializer,
)


class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = propertyType.objects.all().order_by('name')
    serializer_class = PropertyTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ApartmentListingViewSet(viewsets.ModelViewSet):
    queryset = apartmentListingModel.objects.all()
    serializer_class = ApartmentListingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class IndividualListingViewSet(viewsets.ModelViewSet):
    queryset = individualListingModel.objects.all().order_by('-created_at')
    serializer_class = IndividualListingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class OptionalIndividualViewSet(viewsets.ModelViewSet):
    queryset = optionalIndividual.objects.all()
    serializer_class = OptionalIndividualSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AmenityViewSet(viewsets.ModelViewSet):
    queryset = amenity.objects.all().order_by('name')
    serializer_class = AmenitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ListingAmenityViewSet(viewsets.ModelViewSet):
    queryset = ListingAmentiy.objects.all()
    serializer_class = ListingAmenitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

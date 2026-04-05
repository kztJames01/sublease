from django.conf import settings
from django.db.models import F
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, status, serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from api.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly, IsApprovedApartmentLister
from .models import (
    propertyType,
    apartmentListingModel,
    individualListingModel,
    optionalIndividual,
    amenity,
    ListingAmentiy,
    ListingImage,
    ListingView,
    ApartmentUnit,
    ApartmentUnitImage,
)
from .serializers import (
    PropertyTypeSerializer,
    ApartmentListingSerializer,
    IndividualListingSerializer,
    OptionalIndividualSerializer,
    AmenitySerializer,
    ListingAmenitySerializer,
    ListingImageSerializer,
    ApartmentUnitSerializer,
)


class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = propertyType.objects.all().order_by('name')
    serializer_class = PropertyTypeSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        for value, _label in propertyType.PROPERTY_CHOICES:
            propertyType.objects.get_or_create(name=value)
        return propertyType.objects.all().order_by('name')


@method_decorator(cache_page(settings.CACHE_TTL), name='list')
@method_decorator(cache_page(settings.CACHE_TTL), name='retrieve')
class ApartmentListingViewSet(viewsets.ModelViewSet):
    queryset = apartmentListingModel.objects.all()
    serializer_class = ApartmentListingSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = apartmentListingModel.objects.all()
        if self.request.query_params.get('mine') == '1' and self.request.user.is_authenticated:
            queryset = queryset.filter(created_by=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[IsApprovedApartmentLister])
    def portal_access(self, request):
        app = apartmentListingModel.objects.filter(created_by=request.user, is_approved=True).order_by('-id').first()
        if not app:
            return Response({'detail': 'Not approved for apartment portal.'}, status=status.HTTP_403_FORBIDDEN)
        return Response({'id': app.id, 'company': app.company, 'is_approved': app.is_approved})


@method_decorator(cache_page(settings.CACHE_TTL), name='list')
@method_decorator(cache_page(settings.CACHE_TTL), name='retrieve')
class IndividualListingViewSet(viewsets.ModelViewSet):
    queryset = individualListingModel.objects.all().order_by('-created_at')
    serializer_class = IndividualListingSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        listing = serializer.save(created_by=self.request.user)
        # Handle gallery images
        for i, f in enumerate(self.request.FILES.getlist('gallery_images')):
            ListingImage.objects.create(listing=listing, image=f, order=i)
        # Handle amenities
        amenity_ids = self.request.data.getlist('amenity_ids') if hasattr(self.request.data, 'getlist') else self.request.data.get('amenity_ids', [])
        for aid in amenity_ids:
            try:
                ListingAmentiy.objects.create(listing=listing, amenity_id=int(aid))
            except (ValueError, amenity.DoesNotExist):
                pass
        amenity_names = self.request.data.getlist('amenity_names') if hasattr(self.request.data, 'getlist') else self.request.data.get('amenity_names', [])
        for name in amenity_names:
            cleaned = str(name).strip()
            if not cleaned:
                continue
            am, _ = amenity.objects.get_or_create(name=cleaned)
            ListingAmentiy.objects.get_or_create(listing=listing, amenity=am)

    def perform_update(self, serializer):
        listing = serializer.save()
        # Replace gallery images if new ones provided
        new_images = self.request.FILES.getlist('gallery_images')
        if new_images:
            listing.gallery_images.all().delete()
            for i, f in enumerate(new_images):
                ListingImage.objects.create(listing=listing, image=f, order=i)
        # Replace amenities if provided
        amenity_ids = self.request.data.getlist('amenity_ids') if hasattr(self.request.data, 'getlist') else self.request.data.get('amenity_ids', [])
        amenity_names = self.request.data.getlist('amenity_names') if hasattr(self.request.data, 'getlist') else self.request.data.get('amenity_names', [])
        if amenity_ids or amenity_names:
            listing.amenities.all().delete()
            for aid in amenity_ids:
                try:
                    ListingAmentiy.objects.create(listing=listing, amenity_id=int(aid))
                except (ValueError, amenity.DoesNotExist):
                    pass
            for name in amenity_names:
                cleaned = str(name).strip()
                if not cleaned:
                    continue
                am, _ = amenity.objects.get_or_create(name=cleaned)
                ListingAmentiy.objects.get_or_create(listing=listing, amenity=am)

    @action(detail=True, methods=['post'])
    def track_click(self, request, pk=None):
        listing = self.get_object()
        user = request.user if request.user.is_authenticated else None

        # Never count owner visits.
        if user and listing.created_by_id == user.id:
            return Response({'counted': False, 'reason': 'owner_view'}, status=status.HTTP_200_OK)

        created = False
        if user:
            _, created = ListingView.objects.get_or_create(listing=listing, viewer=user)
        else:
            visitor_token = (
                str(request.data.get('visitor_token', '')).strip()
                or str(request.headers.get('X-Visitor-Token', '')).strip()
            )
            if visitor_token:
                _, created = ListingView.objects.get_or_create(
                    listing=listing,
                    viewer=None,
                    visitor_token=visitor_token[:64],
                )

        if created:
            individualListingModel.objects.filter(pk=pk).update(clicks_count=F('clicks_count') + 1)

        return Response({'counted': created}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def track_inquiry(self, request, pk=None):
        individualListingModel.objects.filter(pk=pk).update(inquiries_count=F('inquiries_count') + 1)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def toggle_like(self, request, pk=None):
        # Simple increment/decrement — a production app would use a junction table
        individualListingModel.objects.filter(pk=pk).update(likes_count=F('likes_count') + 1)
        return Response(status=status.HTTP_204_NO_CONTENT)


class OptionalIndividualViewSet(viewsets.ModelViewSet):
    queryset = optionalIndividual.objects.all()
    serializer_class = OptionalIndividualSerializer
    permission_classes = [IsAdminOrReadOnly]


@method_decorator(cache_page(settings.CACHE_TTL), name='list')
@method_decorator(cache_page(settings.CACHE_TTL), name='retrieve')
class AmenityViewSet(viewsets.ModelViewSet):
    queryset = amenity.objects.all().order_by('name')
    serializer_class = AmenitySerializer
    permission_classes = [IsAdminOrReadOnly]


class ListingAmenityViewSet(viewsets.ModelViewSet):
    queryset = ListingAmentiy.objects.all()
    serializer_class = ListingAmenitySerializer
    permission_classes = [IsAdminOrReadOnly]


class ApartmentUnitViewSet(viewsets.ModelViewSet):
    serializer_class = ApartmentUnitSerializer
    permission_classes = [IsApprovedApartmentLister]

    def get_queryset(self):
        return ApartmentUnit.objects.filter(created_by=self.request.user).select_related('apartment')

    def perform_create(self, serializer):
        apartment = apartmentListingModel.objects.filter(created_by=self.request.user, is_approved=True).order_by('-id').first()
        if apartment is None:
            raise serializers.ValidationError({'detail': 'Apartment portal access not approved.'})
        unit = serializer.save(created_by=self.request.user, apartment=apartment)
        for i, f in enumerate(self.request.FILES.getlist('gallery_images')):
            ApartmentUnitImage.objects.create(unit=unit, image=f, order=i)

    def perform_update(self, serializer):
        unit = serializer.save()
        new_images = self.request.FILES.getlist('gallery_images')
        if new_images:
            unit.gallery_images.all().delete()
            for i, f in enumerate(new_images):
                ApartmentUnitImage.objects.create(unit=unit, image=f, order=i)

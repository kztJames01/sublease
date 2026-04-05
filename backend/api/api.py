from django.urls import path, include
from rest_framework.routers import DefaultRouter

from item.api import CategoryViewSet, ItemViewSet
from Listing.api import (
    PropertyTypeViewSet,
    ApartmentListingViewSet,
    IndividualListingViewSet,
    OptionalIndividualViewSet,
    AmenityViewSet,
    ListingAmenityViewSet,
)
from communication.api import ConversationViewSet, ConversationMessageViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'items', ItemViewSet)
router.register(r'property-types', PropertyTypeViewSet)
router.register(r'apartment-listings', ApartmentListingViewSet)
router.register(r'individual-listings', IndividualListingViewSet)
router.register(r'individual-optional-details', OptionalIndividualViewSet)
router.register(r'amenities', AmenityViewSet)
router.register(r'listing-amenities', ListingAmenityViewSet)
router.register(r'conversations', ConversationViewSet)
router.register(r'conversation-messages', ConversationMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

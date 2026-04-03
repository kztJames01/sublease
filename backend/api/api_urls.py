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
from . import auth_api

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'items', ItemViewSet)
router.register(r'property-types', PropertyTypeViewSet)
router.register(r'apartment-listings', ApartmentListingViewSet)
router.register(r'individual-listings', IndividualListingViewSet)
router.register(r'individual-optional-details', OptionalIndividualViewSet)
router.register(r'amenities', AmenityViewSet)
router.register(r'listing-amenities', ListingAmenityViewSet)
router.register(r'conversations', ConversationViewSet, basename='conversations')
router.register(r'conversation-messages', ConversationMessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('', include(router.urls)),
    # Auth endpoints
    path('auth/csrf/', auth_api.get_csrf_token, name='api-csrf'),
    path('auth/login/', auth_api.login_view, name='api-login'),
    path('auth/signup/', auth_api.signup_view, name='api-signup'),
    path('auth/logout/', auth_api.logout_view, name='api-logout'),
    path('auth/user/', auth_api.user_view, name='api-user'),
    path('auth/password-reset/', auth_api.password_reset_view, name='api-password-reset'),
    path('auth/providers/', auth_api.oauth_providers_view, name='api-oauth-providers'),
]

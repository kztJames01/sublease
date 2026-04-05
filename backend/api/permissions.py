from rest_framework.permissions import SAFE_METHODS, BasePermission
from Listing.models import apartmentListingModel


class IsOwnerOrReadOnly(BasePermission):
    """Allow writes only to the owner via `created_by`."""

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return getattr(obj, 'created_by_id', None) == getattr(request.user, 'id', None)


class IsAdminOrReadOnly(BasePermission):
    """Allow public reads, but restrict writes to admins."""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsApprovedApartmentLister(BasePermission):
    """Only approved apartment applicants can manage apartment unit portal data."""

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return apartmentListingModel.objects.filter(created_by=request.user, is_approved=True).exists()

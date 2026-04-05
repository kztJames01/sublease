from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets

from api.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer


@method_decorator(cache_page(settings.CACHE_TTL), name='list')
@method_decorator(cache_page(settings.CACHE_TTL), name='retrieve')
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


@method_decorator(cache_page(settings.CACHE_TTL), name='list')
@method_decorator(cache_page(settings.CACHE_TTL), name='retrieve')
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('-created_at')
    serializer_class = ItemSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

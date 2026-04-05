from rest_framework import serializers

from .models import (
    propertyType,
    apartmentListingModel,
    individualListingModel,
    optionalIndividual,
    amenity,
    ListingAmentiy,
    ListingImage,
    ApartmentUnit,
    ApartmentUnitImage,
)


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = propertyType
        fields = ('id', 'name')


class ApartmentListingSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        website_url = attrs.get('website_url', getattr(self.instance, 'website_url', ''))
        if not website_url or not str(website_url).strip():
            raise serializers.ValidationError({'website_url': 'Website URL is required.'})
        return attrs

    class Meta:
        model = apartmentListingModel
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'company',
            'city',
            'zipCode',
            'state',
            'country',
            'website_url',
            'is_approved',
            'created_by',
        )
        read_only_fields = ('created_by', 'is_approved')


class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = ('id', 'image', 'order')


class ApartmentUnitImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentUnitImage
        fields = ('id', 'image', 'order')


class ApartmentUnitSerializer(serializers.ModelSerializer):
    gallery_images = ApartmentUnitImageSerializer(many=True, read_only=True)

    class Meta:
        model = ApartmentUnit
        fields = (
            'id',
            'apartment',
            'created_by',
            'title',
            'unit_code',
            'bedrooms',
            'bathrooms',
            'price',
            'description',
            'website_url',
            'cover_image',
            'video',
            'is_active',
            'gallery_images',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_by', 'created_at', 'updated_at')


class IndividualListingSerializer(serializers.ModelSerializer):
    property_type_name = serializers.CharField(source='property_type.name', read_only=True)
    gallery_images = ListingImageSerializer(many=True, read_only=True)
    amenity_ids = serializers.SerializerMethodField()

    class Meta:
        model = individualListingModel
        fields = (
            'id',
            'images',
            'video',
            'property_type',
            'property_type_name',
            'created_by',
            'bedrooms',
            'bedroom_privacy',
            'bathrooms',
            'bathroom_privacy',
            'address',
            'description',
            'price',
            'title',
            'website_url',
            'is_sold',
            'is_saved',
            'created_at',
            'likes_count',
            'clicks_count',
            'inquiries_count',
            'offer_status',
            'gallery_images',
            'amenity_ids',
        )
        read_only_fields = ('created_by', 'created_at', 'likes_count', 'clicks_count', 'inquiries_count')

    def get_amenity_ids(self, obj):
        return list(obj.amenities.values_list('amenity_id', flat=True))

    def validate(self, attrs):
        errors = {}
        instance = getattr(self, 'instance', None)

        images = attrs.get('images', getattr(instance, 'images', None))
        description = attrs.get('description', getattr(instance, 'description', None))
        website_url = attrs.get('website_url', getattr(instance, 'website_url', ''))

        if not images:
            errors['images'] = 'Image is required.'
        if not description or not str(description).strip():
            errors['description'] = 'Description is required.'
        if not website_url or not str(website_url).strip():
            errors['website_url'] = 'Website URL is required.'

        if errors:
            raise serializers.ValidationError(errors)

        return attrs


class OptionalIndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = optionalIndividual
        fields = (
            'id',
            'listing',
            'squarefeet',
            'LaundryType',
            'parking',
            'air_Conditioning',
            'heating',
        )


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = amenity
        fields = ('id', 'name')


class ListingAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingAmentiy
        fields = ('id', 'listing', 'amenity')

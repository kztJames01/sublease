from rest_framework import serializers

from .models import (
    propertyType,
    apartmentListingModel,
    individualListingModel,
    optionalIndividual,
    amenity,
    ListingAmentiy,
)


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = propertyType
        fields = ('id', 'name')


class ApartmentListingSerializer(serializers.ModelSerializer):
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
            'created_by',
        )
        read_only_fields = ('created_by',)


class IndividualListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = individualListingModel
        fields = (
            'id',
            'images',
            'video',
            'property_type',
            'created_by',
            'bedrooms',
            'bathrooms',
            'address',
            'description',
            'price',
            'title',
            'is_sold',
            'is_saved',
            'created_at',
        )
        read_only_fields = ('created_by', 'created_at')


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

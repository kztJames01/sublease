from django.db import models
from django.contrib.auth.models import User


#import user to create a user from models

# Create your models here.

class propertyType(models.Model):
    TOWNHOUSE = 'Townhouse'
    OFF_CAMPUS_APARTMENT = 'Off-campus Apartment'
    ON_CAMPUS_DORM = 'On-campus Dorm'
    PROPERTY_CHOICES = [
        (TOWNHOUSE, 'Townhouse'),
        (OFF_CAMPUS_APARTMENT, 'Off-campus Apartment'),
        (ON_CAMPUS_DORM, 'On-campus Dorm'),
    ]

    name = models.CharField(max_length=255, unique=True, choices=PROPERTY_CHOICES)
    #spelling for the plural category
    #also fix the name of the database items and ordering them
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.name
    

class apartmentListingModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipCode = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    website_url = models.URLField(max_length=500)
    is_approved = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name = 'apartments',on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.company} - {self.city}"


class individualListingModel(models.Model):
    SHARED = 'shared'
    PRIVATE = 'private'
    PRIVACY_CHOICES = [
        (SHARED, 'Shared'),
        (PRIVATE, 'Private'),
    ]

    PENDING = 'pending'
    ACCEPTING = 'accepting'
    CLOSED = 'closed'
    OFFER_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTING, 'Accepting Offers'),
        (CLOSED, 'Closed'),
    ]

    images = models.ImageField(upload_to = 'iListing_images',blank=True,null = True)
    video = models.FileField(upload_to = 'iListing_video',blank=True,null = True)
    property_type = models.ForeignKey(propertyType,related_name = 'property',on_delete = models.CASCADE)
    created_by = models.ForeignKey(User,related_name = 'IndividualListings',on_delete = models.CASCADE)
    bedrooms = models.IntegerField()
    bedroom_privacy = models.CharField(max_length=20, choices=PRIVACY_CHOICES, default=PRIVATE)
    bathrooms = models.IntegerField()
    bathroom_privacy = models.CharField(max_length=20, choices=PRIVACY_CHOICES, default=PRIVATE)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    title = models.CharField(max_length=255)
    website_url = models.URLField(max_length=500, blank=True, default='')
    is_sold = models.BooleanField(default=False)
    is_saved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # Stats
    likes_count = models.PositiveIntegerField(default=0)
    clicks_count = models.PositiveIntegerField(default=0)
    inquiries_count = models.PositiveIntegerField(default=0)
    offer_status = models.CharField(max_length=20, choices=OFFER_STATUS_CHOICES, default=ACCEPTING)

    def __str__(self):
        return self.title


class ListingImage(models.Model):
    listing = models.ForeignKey(individualListingModel, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='iListing_images')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return f"Image {self.order} for {self.listing.title}"

class optionalIndividual(models.Model):
     listing = models.ForeignKey(individualListingModel,related_name = 'optional_details',on_delete = models.CASCADE)
     squarefeet = models.FloatField()
     LaundryType = models.CharField(max_length=255)
     parking = models.CharField(max_length=255)
     air_Conditioning = models.CharField(max_length=255)
     heating = models.CharField(max_length=255)

class amenity(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ListingAmentiy(models.Model):
    listing = models.ForeignKey(individualListingModel,related_name = 'amenities',on_delete = models.CASCADE)
    amenity = models.ForeignKey(amenity,related_name = 'listings',on_delete = models.CASCADE)

class ListingView(models.Model):
    listing = models.ForeignKey(individualListingModel, related_name='unique_views', on_delete=models.CASCADE)
    viewer = models.ForeignKey(User, related_name='listing_views', on_delete=models.CASCADE, null=True, blank=True)
    visitor_token = models.CharField(max_length=64, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['listing', 'viewer'],
                condition=models.Q(viewer__isnull=False),
                name='unique_listing_view_per_user',
            ),
            models.UniqueConstraint(
                fields=['listing', 'visitor_token'],
                condition=models.Q(viewer__isnull=True) & ~models.Q(visitor_token=''),
                name='unique_listing_view_per_visitor_token',
            ),
        ]


class ApartmentUnit(models.Model):
    apartment = models.ForeignKey(apartmentListingModel, related_name='units', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='apartment_units', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    unit_code = models.CharField(max_length=50)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    website_url = models.URLField(max_length=500, blank=True, default='')
    cover_image = models.ImageField(upload_to='apartment_unit_images', blank=True, null=True)
    video = models.FileField(upload_to='apartment_unit_video', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated_at',)

    def __str__(self):
        return f'{self.title} ({self.unit_code})'


class ApartmentUnitImage(models.Model):
    unit = models.ForeignKey(ApartmentUnit, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='apartment_unit_images')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('order',)

    

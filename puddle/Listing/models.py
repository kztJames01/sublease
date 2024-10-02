from django.db import models

#import user to create a user from models
from django.contrib.auth.models import User
# Create your models here.

class propertyType(models.Model):
    name = models.CharField(max_length=255)
    #spelling for the plural category
    #also fix the name of the database items and ordering them
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

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
    created_by = models.ForeignKey(User,related_name = 'apartments',on_delete = models.CASCADE)


class individualListingModel(models.Model):
    images = models.ImageField(upload_to = 'iListing_images',blank=True,null = True)
    video = models.FileField(upload_to = 'iListing_video',blank=True,null = True)
    property_type = models.ForeignKey(propertyType,related_name = 'property',on_delete = models.CASCADE)
    created_by = models.ForeignKey(User,related_name = 'IndividualListings',on_delete = models.CASCADE)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    is_saved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class optionalIndividual(models.Model):
     listing = models.ForeignKey(individualListingModel,related_name = 'optional_details',on_delete = models.CASCADE)
     squarefeet = models.FloatField()
     LaundryType = models.CharField(max_length=255)
     parking = models.CharField(max_length=255)
     air_Conditioning = models.CharField(max_length=255)
     heating = models.CharField(max_length=255)

class amenity(models.Model):
    name = models.CharField(max_length=255)

class ListingAmentiy(models.Model):
    listing = models.ForeignKey(individualListingModel,related_name = 'amenities',on_delete = models.CASCADE)
    amenity = models.ForeignKey(amenity,related_name = 'listings',on_delete = models.CASCADE)

    
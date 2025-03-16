from django.db import models
#import user to create a user from models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):

    is_student = models.BooleanField(default=False)
    is_renter = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)

    def __str__(self):
        return self.username



    

    

from django.db import models
#import user to create a user from models
from django.contrib.auth.models import User
# Create your models here.
# Category data model for the site

class Category(models.Model):
    name = models.CharField(max_length=255)
    #spelling for the plural category
    #also fix the name of the database items and ordering them
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name = 'items',on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to = 'item_images',blank=True,null = True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name = 'items',on_delete = models.CASCADE)

    def __str__(self):
        return self.name
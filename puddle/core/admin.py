from django.contrib import admin

# Register your models here.
# use .models due to the same folder as admin.py
from .models import Category, Item

admin.site.register(Category)
admin.site.register(Item)
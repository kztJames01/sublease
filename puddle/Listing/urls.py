from django.urls import path
from . import views

app_name = 'Listing'
urlpatterns = [
    path('createListing/',views.createListing,name = 'createListing'),
    path('createListing/newAL/',views.newAL,name = 'newAL'),
    path('createListing/newIL/',views.newIL,name = 'newIL'),
]
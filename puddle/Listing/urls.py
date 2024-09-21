from django.urls import path
from . import views

app_name = 'Listing'
urlpatterns = [
    path('createListing/',views.createListing,name = 'createListing'),

]
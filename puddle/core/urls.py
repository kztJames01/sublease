from django.urls import path
from . import views
app_name = 'core'

urlpatterns = [
    path('',views.base, name = 'base'), 
    path('search/',views.search, name = 'search'),
    path('contact/',views.contact,name = 'contact'),
    
]
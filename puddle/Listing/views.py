from django.shortcuts import render

# Create your views here.
def createListing(request):
    return render(request, 'Listing/createListing.html')
from django.shortcuts import get_object_or_404,  render
from django.contrib.auth.decorators import login_required
from .forms import NewIListingForm, NewAListingForm
from .models import individualListingModel
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.
def createListing(request):
    return render(request, 'Listing/createListing.html')

def detail(request,pk):
    item = get_object_or_404(individualListingModel,pk=pk)
    related_items = individualListingModel.objects.filter(category=item.property_type, is_sold = False).exclude(pk=pk)[0:6]
    return render(request,'Listing/iListingDetail.html',{
        'item':item,
        'related_items':related_items,
    })
@login_required
def newAL(request):
    if request.method == 'POST':
        form = NewAListingForm(request.POST)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            
    form = NewIListingForm()

    return render(request, 'Listing/apartmentListing.html',{
        'form' :form,
    })

@login_required
def newIL(request):
    if request.method == 'POST':
        form = NewIListingForm(request.POST,request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            
    form = NewIListingForm()

    return render(request, 'Listing/individualListing.html',{
        'form' :form,
    })

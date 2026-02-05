from django.shortcuts import get_object_or_404,  render
from django.contrib.auth.decorators import login_required
from .forms import NewIListingForm, NewAListingForm
from .models import individualListingModel

# Create your views here.
def createListing(request):
    return render(request, 'Listing/createListing.html',{
        'show': False,
    })

def detail(request,pk):
    item = get_object_or_404(individualListingModel,pk=pk)
    related_items = individualListingModel.objects.filter(property_type=item.property_type, is_sold=False).exclude(pk=pk)[0:6]
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
            return render(request, 'Listing/apartmentListing.html',{
                'form' : NewAListingForm(),
                'show': True,
            })
            
            form = NewAListingForm()

    return render(request, 'Listing/apartmentListing.html',{
        'form' :form,
        'show': False,
    })

@login_required
def newIL(request):
    if request.method == 'POST':
        form = NewIListingForm(request.POST,request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return render(request, 'Listing/individualListing.html',{
                'form' : NewIListingForm(),
                'show': True,
            })

            
    form = NewIListingForm()

    return render(request, 'Listing/individualListing.html',{
        'form' :form,
        'show': False,
    })

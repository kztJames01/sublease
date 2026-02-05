from django import forms

from .models import individualListingModel, apartmentListingModel, propertyType
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewIListingForm(forms.ModelForm):
    class Meta:
        model = individualListingModel
        fields = ('property_type', 'title', 'bedrooms', 'bathrooms', 'description', 'price', 'images', 'video')
    
    video = forms.FileField(widget = forms.FileInput(attrs={
        'placeholder' : 'Add your video here',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))

    images = forms.FileField(widget = forms.FileInput(attrs={
        
        'placeholder' : 'Add your images here',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))

    property_type = forms.ModelChoiceField(
        queryset=propertyType.objects.all(),
        widget=forms.Select(attrs={
            'class': 'w-full py-4 px-6 rounded-xl'
        })
    )
    title = forms.CharField(widget = forms.TextInput(attrs={
        'placeholder' : 'Enter your caption',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))

    description = forms.CharField(widget = forms.Textarea(attrs={
        'placeholder' : 'Enter your description',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))

    bedrooms = forms.IntegerField(widget = forms.NumberInput(attrs={
        'placeholder' : 'Number of bedrooms',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))

    bathrooms = forms.IntegerField(widget = forms.NumberInput(attrs={
        'placeholder' : 'Number of bathrooms',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))

    price = forms.CharField(widget = forms.NumberInput(attrs={
        'placeholder' : 'Enter your price',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))

class NewAListingForm(forms.ModelForm):
    class Meta:
        model = apartmentListingModel
        fields = ('first_name', 'last_name', 'email', 'phone', 'company', 'city', 'zipCode', 'state', 'country')

        widgets = {
            'first_name' : forms.TextInput(attrs = {
                'class': INPUT_CLASSES
            }),
            'last_name' : forms.TextInput(attrs = {
                'class': INPUT_CLASSES
            }),
            'email' : forms.EmailInput(attrs = {
                'class': INPUT_CLASSES
            }),
            'phone' : forms.NumberInput(attrs = {
                'class': INPUT_CLASSES
            }),
            'company' : forms.TextInput(attrs = {
                'class': INPUT_CLASSES
            }),
            'city' : forms.TextInput(attrs = {
                'class': INPUT_CLASSES
            }),
            'zipCode' : forms.NumberInput(attrs = {
                'class': INPUT_CLASSES
            }),
            'state' : forms.SelectMultiple(attrs = {
                'class': INPUT_CLASSES
            }),
            'country' : forms.SelectMultiple(attrs = {
                'class': INPUT_CLASSES
            }),
        }
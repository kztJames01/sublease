from django import forms

from .models import individualListingModel,apartmentListingModel
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewIListingForm(forms.ModelForm):
    class Meta:
        model = individualListingModel
        fields = ('bedrooms','bathrooms','address','description','price','images','video',)
        widgets = {
            'address' : forms.TextInput(attrs = {
                'class': INPUT_CLASSES
            }),
            'description' : forms.Textarea(attrs = {
                'class': INPUT_CLASSES
            }),
            'price' : forms.TextInput(attrs = {
                'class': INPUT_CLASSES
            }),
            'bedrooms' : forms.TextInput(attrs = {
                'class': INPUT_CLASSES
            }),
            'bathrooms' : forms.TextInput(attrs = {
                'class': INPUT_CLASSES
            }),
            'images' : forms.FileInput(attrs = {
                'class': INPUT_CLASSES
            }),
            'video' : forms.FileInput(attrs = {
                'class': INPUT_CLASSES
            }),
        }


class NewAListingForm(forms.ModelForm):
    class Meta:
        model = apartmentListingModel
        fields = {'first_name','last_name','email','phone','company','city','zipCode','state','country',}

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
from django.shortcuts import render, redirect
#to be able to view the database models 
# you have to import them from models to core.views file
from .forms import SignupForm
from .models import Category, Item
# Create your views here.
def base(request):

    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
        else:
            form = SignupForm()
    form = SignupForm()
    return render(request,'core/signup.html',{
        'form':form
    })

def login(request):
    return render(request, 'core/base.html')


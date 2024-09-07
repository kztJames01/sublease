from django.shortcuts import render, redirect
#to be able to view the database models 
# you have to import them from models to core.views file
from .forms import SignupForm
from .models import Category, Item
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'categories':categories,
        'items':items,
    })

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
from django.shortcuts import render, redirect
#to be able to view the database models 
# you have to import them from models to core.views file
from .forms import SignupForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def base(request):
    return render(request, 'core/index.html', {
        'range_values':range(1,6),
        'left':True,
        'reviewList':review_list
    })
def search(request):
    
    return render(request, 'core/listing.html',{
        'range_values':range(1,6),
    })
def contact(request):
    return render(request, 'core/contact.html')

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'core/registration/password_reset_form.html'
    subject_template_name = 'core/registration/reset_subject.txt'
    email_template_name = 'core/registration/password_reset_email.html'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the email address you registered with and check your spam folder."
    success_url = reverse_lazy('core:base')



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/accounts/login/')
        else:
            form = SignupForm()

    else:
        form = SignupForm()       
    return render(request,'core/registration/signup.html',{
        'form':form
    })

def login(request):
    return render(request, 'core/index.html',
        {'range_values':range(1,6),
         'left':True,
        'review_list':review_list
    })


def logout_view(request):
    logout(request)

    return redirect('/')


review_list = [
    {
        "name": "Alice Johnson",
        "review": "lvSpace helped me find the perfect apartment right next to campus! The search filters made it easy to find what I wanted.",
        "features": ["User-friendly interface", "Great search filters", "Fast response times"]
    },
    {
        "name": "Mark Stevens",
        "review": "Listing my sublease on lvSpace was a breeze! The platform is intuitive and made connecting with potential renters so simple.",
        "features": ["Easy listing process", "Effective communication tools", "Attractive layout"]
    },
    {
        "name": "Jessica Lee",
        "review": "I love how lvSpace allows students to find affordable housing options! The community feedback helped me make the best choice.",
        "features": ["Affordable options", "Community-driven reviews", "Helpful support"]
    },
    {
        "name": "David Smith",
        "review": "The variety of listings on lvSpace is impressive! I was able to find a place that fit my budget and needs perfectly.",
        "features": ["Diverse listings", "Budget-friendly options", "Detailed descriptions"]
    },
    {
        "name": "Samantha Green",
        "review": "As a first-time renter, I found lvSpace extremely helpful. The tips and resources provided made the process so much easier.",
        "features": ["Helpful resources", "Guidance for first-time renters", "Supportive community"]
    },
    {
        "name": "Michael Brown",
        "review": "lvSpace is a game changer! I found my sublease within days and the platform made the whole process stress-free.",
        "features": ["Quick listings", "Stress-free process", "Great customer service"]
    },
    {
        "name": "Emma Davis",
        "review": "What I appreciate most about lvSpace is the ability to communicate directly with landlords. It made my search much smoother.",
        "features": ["Direct communication", "Smooth process", "Trustworthy listings"]
    },
    {
        "name": "Lucas White",
        "review": "I had a fantastic experience using lvSpace. The apartment I found exceeded my expectations and the management was very responsive.",
        "features": ["Responsive management", "Exceeds expectations", "Positive experience"]
    }
]

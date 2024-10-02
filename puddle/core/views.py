from django.shortcuts import render, redirect
#to be able to view the database models 
# you have to import them from models to core.views file
from .forms import SignupForm, ResetPaswordForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

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

def faq(request):
    return render(request, 'core/faq.html', {
        'faqs': faqs
    })

class ResetPasswordView(PasswordResetView):
    template_name = 'core/registration/password_reset_form.html'
    subject_template_name = 'core/registration/reset_subject.txt'
    from_email = 'kxt9866@mavs.uta.edu'
    form_class = ResetPaswordForm
    html_email_template_name = 'core/registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            self.send_mail(email, user)
            messages.success(self.request, "We've emailed you instructions for setting your password.")
        except User.DoesNotExist:
            messages.warning(self.request, "If an account exists with this email, instructions have been sent.")
        return super().form_valid(form)

    def send_mail(self, email,user):
        subject = loader.render_to_string(self.subject_template_name).strip()
        context = {
        'email': email,
        'domain': self.request.get_host(),
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
        'protocol': 'https' if self.request.is_secure() else 'http',
        }
        body = loader.render_to_string(self.html_email_template_name, context)
        
        email_message = EmailMultiAlternatives(subject, body, self.from_email, [email])
        email_message.send()

    


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

faqs= [
        {
            "question": "What is lvSpace?",
            "answer": "lvSpace is a platform designed for students to find apartments and subleases near their desired cities or universities. It also allows apartment owners to list their properties."
        },
        {
            "question": "How does the listing process work?",
            "answer": "Apartment owners can easily list their apartments or subleases by creating an account on lvSpace, filling out property details, and uploading images. The process is quick and user-friendly."
        },
        {
            "question": "Is there a fee to list my apartment on lvSpace?",
            "answer": "Yes, we charge a fee based on the number of apartments you are listing. It’s 3% for listings with 50 to 100 units, 5% for 100 to 200 units, and 10% for 200 or more. Students listing subleases pay only 1%."
        },
        {
            "question": "How can students communicate with apartment owners?",
            "answer": "Our platform features a built-in chat function, allowing tenants and owners to communicate in real-time to discuss details about the property."
        },
        {
            "question": "Are there any additional fees for students looking for subleases?",
            "answer": "Students only pay a 1% fee on their sublease listing price. This makes it affordable for students to list their available spaces."
        },
        {
            "question": "How do I find apartments near my university?",
            "answer": "Simply enter your desired city or university into the search bar on our homepage, and you’ll be presented with a list of available apartments and subleases in that area."
        },
        {
            "question": "What kind of properties can I list on lvSpace?",
            "answer": "You can list any type of residential property, including apartments, houses, and subleases, as long as they meet our community guidelines."
        },
        {
            "question": "Can I edit or delete my listing after it's been posted?",
            "answer": "Yes, you have the ability to edit or delete your listing at any time through your account dashboard."
        },
        {
            "question": "What happens if I encounter an issue while using the platform?",
            "answer": "If you face any issues, you can contact our customer support team via the help section on our website. We’re here to assist you!"
        },
        {
            "question": "How does lvSpace ensure a safe and trustworthy environment for users?",
            "answer": "We prioritize user safety by verifying listings and offering a chat feature for direct communication. We encourage users to report any suspicious activity to help maintain a safe community."
        }
    ]
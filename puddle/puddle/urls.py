"""
URL configuration for puddle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from core.views import signup, logout_view, ResetPasswordView
from core.forms import LoginForm
urlpatterns = [
    path('',include('core.urls')),
    path('inbox/',include('communication.urls')),
    path('listing/',include('Listing.urls')),
    path('items/',include('item.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('accounts/signup/',signup, name = 'signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name = 'core/registration/login.html',authentication_form=LoginForm),name = 'login'),
    path('accounts/logout/', logout_view,name = 'logout'),
    path('accounts/password-reset/', ResetPasswordView.as_view(template_name = 'core/registration/password_reset_form.html',),name = 'password_reset'),
    
    path('accounts/password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'core/registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='core/registration/password_reset_complete.html'),name='password_reset_complete'),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

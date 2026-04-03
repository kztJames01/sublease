import re

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle


class AuthRateThrottle(AnonRateThrottle):
    rate = '10/minute'


def _user_payload(user):
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }


@api_view(['GET'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def get_csrf_token(request):
    return Response({'csrfToken': get_token(request)})


@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([AuthRateThrottle])
def login_view(request):
    username = request.data.get('username', '').strip()
    password = request.data.get('password', '')
    if not username or not password:
        return Response(
            {'error': 'Username and password are required.'},
            status=status.HTTP_400_BAD_REQUEST,
        )
    user = authenticate(request, username=username, password=password)
    if user is None:
        return Response(
            {'error': 'Invalid credentials.'},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    login(request, user)
    return Response({'user': _user_payload(user)})


@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([AuthRateThrottle])
def signup_view(request):
    first_name = request.data.get('first_name', '').strip()
    last_name = request.data.get('last_name', '').strip()
    email = request.data.get('email', '').strip()
    password = request.data.get('password', '')
    agree_terms = request.data.get('agree_terms', False)

    errors = {}
    if not first_name:
        errors['first_name'] = 'First name is required.'
    if not last_name:
        errors['last_name'] = 'Last name is required.'
    if not email:
        errors['email'] = 'Email is required.'
    else:
        try:
            validate_email(email)
        except ValidationError:
            errors['email'] = 'Enter a valid email address.'
    if not password:
        errors['password'] = 'Password is required.'
    if not agree_terms:
        errors['agree_terms'] = 'You must agree to the terms and conditions.'

    if errors:
        return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

    # Validate password strength
    try:
        validate_password(password)
    except ValidationError as e:
        return Response(
            {'errors': {'password': list(e.messages)}},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if User.objects.filter(email__iexact=email).exists():
        return Response(
            {'errors': {'email': 'Email already registered.'}},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Generate username from email prefix
    base_username = re.sub(r'[^a-zA-Z0-9]', '', email.split('@')[0])[:20]
    username = base_username
    counter = 1
    while User.objects.filter(username=username).exists():
        username = f'{base_username}{counter}'
        counter += 1

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )
    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    return Response({'user': _user_payload(user)}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'detail': 'Logged out.'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_view(request):
    return Response(_user_payload(request.user))


@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([AuthRateThrottle])
def password_reset_view(request):
    from django.contrib.auth.forms import PasswordResetForm

    email = request.data.get('email', '').strip()
    if not email:
        return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)
    form = PasswordResetForm(data={'email': email})
    if form.is_valid():
        form.save(
            request=request,
            use_https=request.is_secure(),
            from_email=settings.DEFAULT_FROM_EMAIL,
        )
    # Always return success to avoid email enumeration
    return Response({'detail': 'If an account exists with that email, a reset link has been sent.'})


@api_view(['GET'])
@permission_classes([AllowAny])
def oauth_providers_view(request):
    """Return which OAuth providers are configured."""
    providers = []
    sp = settings.SOCIALACCOUNT_PROVIDERS
    if sp.get('google', {}).get('APP', {}).get('client_id'):
        providers.append({'id': 'google', 'name': 'Google'})
    if sp.get('apple', {}).get('APP', {}).get('client_id'):
        providers.append({'id': 'apple', 'name': 'Apple'})
    if sp.get('facebook', {}).get('APP', {}).get('client_id'):
        providers.append({'id': 'facebook', 'name': 'Facebook'})
    return Response({'providers': providers})

import re

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import SimpleRateThrottle
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken


class AuthRateThrottle(SimpleRateThrottle):
    scope = 'auth'

    def get_cache_key(self, request, view):
        ident = self.get_ident(request)
        return self.cache_format % {'scope': self.scope, 'ident': ident}


def _user_payload(user):
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }


def _set_refresh_cookie(response, refresh_token):
    response.set_cookie(
        settings.JWT_REFRESH_COOKIE_NAME,
        str(refresh_token),
        httponly=settings.JWT_REFRESH_COOKIE_HTTPONLY,
        secure=settings.JWT_REFRESH_COOKIE_SECURE,
        samesite=settings.JWT_REFRESH_COOKIE_SAMESITE,
        path=settings.JWT_REFRESH_COOKIE_PATH,
        domain=settings.JWT_REFRESH_COOKIE_DOMAIN,
        max_age=int(settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds()),
    )


def _clear_refresh_cookie(response):
    response.delete_cookie(
        settings.JWT_REFRESH_COOKIE_NAME,
        path=settings.JWT_REFRESH_COOKIE_PATH,
        domain=settings.JWT_REFRESH_COOKIE_DOMAIN,
        samesite=settings.JWT_REFRESH_COOKIE_SAMESITE,
    )


def _issue_auth_response(user, status_code=status.HTTP_200_OK):
    refresh = RefreshToken.for_user(user)
    response = Response(
        {
            'user': _user_payload(user),
            'accessToken': str(refresh.access_token),
        },
        status=status_code,
    )
    _set_refresh_cookie(response, refresh)
    return response


@api_view(['GET'])
@permission_classes([AllowAny])
def get_csrf_token(request):
    return Response({'detail': 'JWT authentication enabled.'})


@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([AuthRateThrottle])
def login_view(request):
    identifier = request.data.get('username', '').strip()
    password = request.data.get('password', '')
    if not identifier or not password:
        return Response(
            {'error': 'Username or email and password are required.'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    username = identifier
    if '@' in identifier:
        matched_user = User.objects.filter(email__iexact=identifier).only('username').first()
        username = matched_user.username if matched_user else identifier

    user = authenticate(request, username=username, password=password)
    if user is None:
        return Response(
            {'error': 'Invalid credentials.'},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    return _issue_auth_response(user)


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

    base_username = re.sub(r'[^a-zA-Z0-9]', '', email.split('@')[0])[:20] or 'user'
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
    return _issue_auth_response(user, status_code=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_view(request):
    refresh_value = request.COOKIES.get(settings.JWT_REFRESH_COOKIE_NAME)
    if not refresh_value:
        return Response({'error': 'Refresh token missing.'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        current_refresh = RefreshToken(refresh_value)
        user_id = current_refresh['user_id']
        user = User.objects.get(id=user_id)
    except (TokenError, User.DoesNotExist, KeyError):
        response = Response({'error': 'Invalid refresh token.'}, status=status.HTTP_401_UNAUTHORIZED)
        _clear_refresh_cookie(response)
        return response

    try:
        if settings.SIMPLE_JWT.get('BLACKLIST_AFTER_ROTATION'):
            current_refresh.blacklist()
    except TokenError:
        pass

    return _issue_auth_response(user)


@api_view(['POST'])
@permission_classes([AllowAny])
def logout_view(request):
    refresh_value = request.COOKIES.get(settings.JWT_REFRESH_COOKIE_NAME)
    if refresh_value:
        try:
            RefreshToken(refresh_value).blacklist()
        except TokenError:
            pass

    response = Response({'detail': 'Logged out.'})
    _clear_refresh_cookie(response)
    return response


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
    return Response({'detail': 'If an account exists with that email, a reset link has been sent.'})


@api_view(['GET'])
@permission_classes([AllowAny])
def oauth_providers_view(request):
    providers = []
    sp = settings.SOCIALACCOUNT_PROVIDERS
    if sp.get('google', {}).get('APP', {}).get('client_id'):
        providers.append({'id': 'google', 'name': 'Google'})
    if sp.get('apple', {}).get('APP', {}).get('client_id'):
        providers.append({'id': 'apple', 'name': 'Apple'})
    if sp.get('facebook', {}).get('APP', {}).get('client_id'):
        providers.append({'id': 'facebook', 'name': 'Facebook'})
    return Response({'providers': providers})

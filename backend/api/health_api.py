from django.core.cache import cache
from django.db import connection
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def healthcheck_view(request):
    status_code = 200
    checks = {'database': 'ok', 'cache': 'ok'}

    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
            cursor.fetchone()
    except Exception:
        checks['database'] = 'error'
        status_code = 503

    try:
        cache.set('healthcheck', 'ok', timeout=5)
        if cache.get('healthcheck') != 'ok':
            raise RuntimeError('cache-read-failed')
    except Exception:
        checks['cache'] = 'error'
        status_code = 503

    return Response({'status': 'ok' if status_code == 200 else 'degraded', 'checks': checks}, status=status_code)

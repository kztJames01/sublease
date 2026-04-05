from typing import Optional

from django.db import connections
from django.db.utils import OperationalError


def get_postgres_connection(alias: str = "default"):
    """Return a live Django-managed PostgreSQL connection or None.

    The project already uses Django's configured database settings. This helper
    provides a safe runtime access point for modules that need a direct
    connection without maintaining a parallel database client.
    """
    try:
        connection = connections[alias]
        connection.ensure_connection()
        return connection
    except (KeyError, OperationalError):
        return None


def get_postgres_cursor(alias: str = "default") -> Optional[object]:
    connection = get_postgres_connection(alias=alias)
    if connection is None:
        return None
    return connection.cursor()


__all__ = ["get_postgres_connection", "get_postgres_cursor"]

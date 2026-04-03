
from typing import Optional
import os
from urllib.parse import quote_plus

# Make pymongo an optional dependency at import time and avoid raising
# during Django startup if Mongo isn't reachable or configured.
try:
    from pymongo.mongo_client import MongoClient
    from pymongo.server_api import ServerApi
except Exception:  # pragma: no cover - optional runtime dependency
    MongoClient = None  # type: ignore
    ServerApi = None  # type: ignore


_client: Optional["MongoClient"] = None
_db = None
collection = None


def get_mongo_collection():
    """Return the `Users` collection or None if a connection cannot be made.

    This function is lazy and safe to call during Django import-time.
    It will not raise on DNS/network errors; callers must handle a None result.
    """
    global _client, _db, collection

    if collection is not None:
        return collection

    if MongoClient is None:
        return None

    username = quote_plus(os.getenv("MONGO_USER", ""))
    password = quote_plus(os.getenv("MONGO_PASSWORD", ""))
    host = os.getenv("MONGO_HOST", "cluster0.ysba7.mongodb.net")
    if not username or not password:
        # Credentials not configured — skip connecting
        return None

    uri = f"mongodb+srv://{username}:{password}@{host}/?retryWrites=true&w=majority&appName=Cluster0"

    try:
        _client = MongoClient(uri, server_api=ServerApi("1"))
        _db = _client.get_database("Authentication")
        collection = _db.get_collection("Users")
        # quick health check
        _client.admin.command("ping")
        return collection
    except Exception:
        # Do not raise during import/startup — return None so Django can continue.
        _client = None
        _db = None
        collection = None
        return None


__all__ = ["get_mongo_collection"]
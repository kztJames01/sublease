import multiprocessing
import os


bind = os.getenv("GUNICORN_BIND", "0.0.0.0:8000")
workers = int(os.getenv("WEB_CONCURRENCY", max(2, multiprocessing.cpu_count() * 2 + 1)))
worker_class = os.getenv("GUNICORN_WORKER_CLASS", "gthread")
threads = int(os.getenv("GUNICORN_THREADS", "4"))
timeout = int(os.getenv("GUNICORN_TIMEOUT", "60"))
keepalive = int(os.getenv("GUNICORN_KEEPALIVE", "5"))
accesslog = "-"
errorlog = "-"
loglevel = os.getenv("GUNICORN_LOG_LEVEL", "info")
forwarded_allow_ips = os.getenv("FORWARDED_ALLOW_IPS", "*")

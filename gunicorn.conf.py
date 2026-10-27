"""Gunicorn settings for production. Run: gunicorn -c gunicorn.conf.py orthoinfo.wsgi:app"""
import os

bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"
workers = int(os.environ.get("WEB_CONCURRENCY", "2"))
threads = 4
timeout = 30
# Load the dataset and build the search index once, then fork: workers share that memory.
preload_app = True
accesslog = "-"
errorlog = "-"

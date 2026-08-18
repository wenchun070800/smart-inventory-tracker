# backend/app/tasks.py
from celery import Celery
import os
from .crud import upsert_counts
from .websocket import broadcast_counts

CELERY_BROKER = os.getenv('CELERY_BROKER', 'redis://redis:6379/0')
celery = Celery('tasks', broker=CELERY_BROKER)

@celery.task
def process_detection(payload):
    ts = payload.get('timestamp')
    counts = payload.get('counts', {})
    device = payload.get('device_id', 'edge-unknown')
    upsert_counts(device, counts, ts)
    # broadcast to websocket clients (non-blocking)
    try:
        broadcast_counts()
    except Exception:
        pass
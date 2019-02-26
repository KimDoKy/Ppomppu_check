import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ppomppu.settings')

app = Celery('conf')

app.config_from_object('django.ppomppu:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task
def add(x, y):
    return x + y
